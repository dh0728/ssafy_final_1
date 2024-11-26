<template>
  <div class="history-container">
    <SideBar />

    <div class="history2-container">
      <!-- 메인 필터 -->
      <div class="main-filters">
        <div class="filter-tabs">
          <button
              class="tab-btn"
              :class="{ active: !showCategoryFilter }"
              @click="toggleTabs(true)"
          >내역 전체보기 ▾</button>
          <button
              class="tab-btn"
              :class="{ active: showCategoryFilter }"
              @click="toggleTabs(false)"
          >카테고리 전체보기 ▾</button>
          <button class="write-btn" @click="openWriteModal">가계부 작성하기 📝</button>
        </div>
      </div>

      <div v-if="showCategoryModal" class="modal-overlay" @click="closeCategoryModal">
        <div class="modal-content" @click.stop>
          <div class="modal-header">
            <h3>카테고리 선택</h3>
            <button class="close-btn" @click="closeCategoryModal">×</button>
          </div>
          <div class="category-list">
            <div class="category-group">
              <button
                  v-for="category in categories"
                  :key="category.id"
                  class="category-item"
                  :class="{ active: selectedCategoryId === category.id }"
                  @click="filterByCategory(category)"
              >
                {{ category.name }}
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 테이블 헤더 -->
      <div class="table-container">
        <table class="history-table">
          <thead>
          <tr>
            <th class="checkbox-col">
              <input type="checkbox">
            </th>
            <th>분류</th>
            <th>날짜</th>
            <th>카테고리</th>
            <th>결제수단</th>
            <th>거래처</th>
            <th>금액</th>
            <th>메모</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="item in paginatedItems" :key="item.account_book_data_id">
            <td><input type="checkbox"></td>
            <td>
      <span :class="['type-badge', item.type]">
        {{ item.type === 'income' ? '수입' : '지출' }}
      </span>
            </td>
            <td>{{ item.date }}</td>
            <td>
              <template v-if="editingItem === item.account_book_data_id">
                <select v-model="item.category_id">
                  <option v-for="cat in categories" :key="cat.id" :value="cat.id">
                    {{ cat.name }}
                  </option>
                </select>
              </template>
              <template v-else>
                {{ getCategoryName(item.category_id) }}
              </template>
            </td>
            <td>
              <template v-if="editingItem === item.account_book_data_id">
                <input v-model="item.payment">
              </template>
              <template v-else>
                {{ item.payment }}
              </template>
            </td>
            <td>
              <template v-if="editingItem === item.account_book_data_id">
                <input v-model="item.store">
              </template>
              <template v-else>
                {{ item.store }}
              </template>
            </td>
            <td>
              <template v-if="editingItem === item.account_book_data_id">
                <input type="number" v-model="item.account">
              </template>
              <template v-else>
                {{ formatNumber(item.account) }}원
              </template>
            </td>
            <td>
              <template v-if="editingItem === item.account_book_data_id">
                <input v-model="item.memo">
              </template>
              <template v-else>
                {{ truncateMemo(item.memo) }}
              </template>
            </td>
            <td class="action-buttons">
              <template v-if="editingItem === item.account_book_data_id">
                <button class="action-btn save" @click="saveEdit(item)">저장</button>
                <button class="action-btn cancel" @click="cancelEdit">취소</button>
              </template>
              <template v-else>
                <button class="action-btn" @click="startEdit(item)">수정하기</button>
                <button class="action-btn delete" @click="deleteItem(item.account_book_data_id)">삭제하기</button>
              </template>
            </td>
          </tr>
          </tbody>
        </table>
      </div>

      <!-- 페이지네이션 -->
      <div class="pagination" v-if="totalPages > 1">
        <button
            class="page-btn"
            :disabled="currentPage === 1"
            @click="changePage(currentPage - 1)"
        >←</button>
        <button
            v-for="page in totalPages"
            :key="page"
            class="page-btn"
            :class="{ active: currentPage === page }"
            @click="changePage(page)"
        >{{ page }}</button>
        <button
            class="page-btn"
            :disabled="currentPage === totalPages"
            @click="changePage(currentPage + 1)"
        >→</button>
      </div>
    </div>
    <CalendarAdd ref="writeModal" :selected-date="currentDate" @write-completed="onWriteCompleted" />
    </div>
</template>

<script setup>
import {onMounted, ref, computed} from 'vue'
import SideBar from "@/components/common/SideBar.vue"
import CalendarAdd from '@/components/calendar/CalendarDateAdd.vue'
import {useCalendarStore} from "@/stores/calendar.js";

const calendarStore = useCalendarStore()
const writeModal = ref(null)
const currentDate = ref(new Date())
const historyItems = ref([])

const showCategoryFilter = ref(false)
const showCategoryModal = ref(false)
const selectedCategoryId = ref(null)

const itemsPerPage = 10  // 페이지당 표시할 아이템 수
const currentPage = ref(1)  // 현재 페이지
const totalPages = computed(() => Math.ceil(filteredHistoryItems.value.length / itemsPerPage))

const editingItem = ref(null)
const tempItem = ref(null)

const categories = ref([
  { id: 1, name: '🏬 모든가맹점' },
  { id: 2, name: '🚍 교통' },
  { id: 3, name: '⛽ 주유' },
  { id: 4, name: '📱 통신' },
  { id: 5, name: '🛒 마트/편의점' },
  { id: 6, name: '🎁 쇼핑' },
  { id: 7, name: '🍛 푸드' },
  { id: 8, name: '☕ 카페/디저트' },
  { id: 9, name: '💄 뷰티/피트니스' },
  { id: 10, name: '💰 무실적' },
  { id: 11, name: '📃 공과금/렌탈' },
  { id: 12, name: '🏥 병원/약국' },
  { id: 13, name: '🐱 애완동물' },
  { id: 14, name: '✏ 교육/육아' },
  { id: 15, name: '🚗 자동차/하이패스' },
  { id: 16, name: '⚽ 레저/스포츠' },
  { id: 17, name: '🎬 영화/문화' },
  { id: 18, name: '🤳 간편결제' },
  { id: 19, name: '✈ 항공마일리지' },
  { id: 20, name: '💺 공항라운지/PP' },
  { id: 21, name: '💎 프리미엄' },
  { id: 22, name: '🧳 여행/숙박' },
  { id: 23, name: '🌏 해외' },
  { id: 24, name: '💼 비지니스' },
  { id: 25, name: '🎸 기타' },
  { id: 26, name: '💸 금융' },
  { id: 27, name: '🏃‍♂️ 생활' }
])

const formatCustomDate = (year, month, day) => {
  return `${year}. ${String(month).padStart(2, '0')}. ${String(day).padStart(2, '0')}`
}

const getCategoryName = (categoryId) => {
  const category = categories.value.find(cat => cat.id === categoryId)
  return category ? category.name : ''
}

const openWriteModal = () => {
  writeModal.value.openModal()
}

// 초기 데이터 로드 시 필터 초기화
const fetchHistoryItems = async () => {
  const year = currentDate.value.getFullYear()
  const month = currentDate.value.getMonth() + 1
  const result = await calendarStore.getYearHistory(year, month)

  if (result) {
    historyItems.value = result.map(item => ({
      ...item,
      type: item.is_income ? 'income' : 'expense',
      date: formatCustomDate(item.year, item.month, item.day),
      amount: item.account
    }))
  }
}

// 삭제 기능
const deleteItem = async (accountBookDataId) => {
  if (confirm('정말 삭제하시겠습니까?')) {
    const success = await calendarStore.deleteCalendar(accountBookDataId)
    if (success) {
      historyItems.value = historyItems.value.filter(
          item => item.account_book_data_id !== accountBookDataId
      )
    }
    await fetchHistoryItems()
  }
}

const formatNumber = (value) => {
  return new Intl.NumberFormat('ko-KR').format(value)
}

// 카테고리 그룹화
const categoryGroups = computed(() => {
  const groups = []
  for (let i = 0; i < categories.value.length; i += 5) {
    groups.push(categories.value.slice(i, i + 5))
  }
  return groups
})

// 필터링된 내역 목록
const filteredHistoryItems = computed(() => {
  if (!selectedCategoryId.value) {
    return historyItems.value
  }
  return historyItems.value.filter(item =>
      item.category_id === selectedCategoryId.value
  )
})

// 카테고리 모달 토글
const toggleCategoryModal = () => {
  showCategoryModal.value = !showCategoryModal.value
  showCategoryFilter.value = true
}

// 카테고리 필터링
const filterByCategory = (category) => {
  selectedCategoryId.value = category.id
  showCategoryModal.value = false
}

// 카테고리 모달 닫기
const closeCategoryModal = () => {
  showCategoryModal.value = false
}

const toggleTabs = (isAllView) => {
  if (isAllView) {
    showCategoryFilter.value = false
    selectedCategoryId.value = null // 카테고리 선택 초기화
  } else {
    toggleCategoryModal()
  }
}


const startEdit = (item) => {
  tempItem.value = {...item}
  editingItem.value = item.account_book_data_id
}

const cancelEdit = () => {
  Object.assign(historyItems.value.find(item => item.account_book_data_id === editingItem.value), tempItem.value)
  editingItem.value = null
}

const saveEdit = async (item) => {
  try {
    const result = await calendarStore.updateCalendar({
      year: item.year,
      month: item.month,
      day: item.day,
      is_income: item.type === 'income',
      payment: item.payment,
      store: item.store,
      category_id: item.category_id,
      account: item.account,
      memo: item.memo,
      account_book_data_id: item.account_book_data_id
    })
    if (result) {
      editingItem.value = null
      await fetchHistoryItems()
    }
  } catch (error) {
    console.error('수정 실패:', error)
  }
}

const truncateMemo = (memo) => {
  return memo.length > 15 ? memo.slice(0, 15) + '...' : memo;
}


// 현재 페이지에 표시할 아이템들
const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return filteredHistoryItems.value.slice(start, end)
})

// 페이지 변경 함수
const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
  }
}

const onWriteCompleted = async () => {
  await fetchHistoryItems()
}

onMounted(() => {
  fetchHistoryItems()
})
</script>

<style scoped>
.history-container {
  padding: 32px;
  margin-left: 440px;
  max-width: 1300px;
  background: white;
}

.history2-container {
  padding: 20px;
  background: white;
}

.write-btn {
  padding: 8px 16px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
}

.main-filters {
  margin-bottom: 20px;
}

.filter-tabs {
  display: flex;
  gap: 12px;
  justify-content: flex-start;
  align-items: center;
}

.write-btn {
  margin-left: 670px;
}

.tab-btn {
  padding: 8px 16px;
  border: none;
  background: none;
  cursor: pointer;
  font-size: 18px;
  font-weight: bold;
  transition: all 0.2s;
}

.tab-btn.active {
  font-weight: 600;
  border-bottom: 2px solid #4C6EF5;
  font-size: 18px
}

.history-table {
  width: 100%;
  border-collapse: collapse;
}

.history-table th {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.history-table td {
  padding: 16px 12px;
  transition: background 0.2s;
}

.history-table tr:hover {
  background: #f8f9fa;
}

.type-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.type-badge.income {
  background: #e8f5e9;
  color: #1BBF83;
}

.type-badge.expense {
  background: #ffebee;
  color: #ff6b6b;
}


.action-buttons {
  display: flex;
  gap: 8px;
}

.action-btn {
  padding: 4px 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
  color: #666;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s;
}

.action-btn:hover {
  background: #f8f9fa;
  border-color: #4C6EF5;
  color: #4C6EF5;
}

.pagination {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 20px;
}

.page-btn {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
}

.page-btn.active {
  background: #4C6EF5;
  color: white;
  border-color: #4C6EF5;
}

.category-item.active {
  background: #4C6EF5;
  color: white;
  border-color: #4C6EF5;
}

.tab-btn {
  position: relative;
  padding: 8px 16px;
  border: none;
  background: none;
  cursor: pointer;
  transition: all 0.2s;
}

.tab-btn.active {
  font-weight: 600;
  border-bottom: 2px solid #4C6EF5;
}

.tab-btn:hover {
  color: #4C6EF5;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.category-list {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
}

.category-item {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
  font-size: 13px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.category-item:hover {
  border-color: #4C6EF5;
  color: #4C6EF5;
}

.category-item.active {
  background: #4C6EF5;
  color: white;
  border-color: #4C6EF5;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: #666;
  cursor: pointer;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 16px;
  padding: 24px;
  width: 800px;
  max-height: 80vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.category-list {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
}

.category-item {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
  font-size: 13px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.category-item:hover {
  border-color: #4C6EF5;
  color: #4C6EF5;
}

.category-item.active {
  background: #4C6EF5;
  color: white;
  border-color: #4C6EF5;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: #666;
  cursor: pointer;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}


.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.modal-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a1438;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: #666;
  cursor: pointer;
}


.category-group {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 16px;
}

.category-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 16px;
}

.category-item {
  padding: 12px;
  border-radius: 12px;
  transition: all 0.3s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.category-item:hover {
  background: #f8f9fa;
  border-color: #4C6EF5;
  color: #4C6EF5;
}

.category-item.active {
  background: #4C6EF5;
  color: white;
  border-color: #4C6EF5;
}

.editable input,
.editable select {
  width: 100%;
  padding: 4px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.editable input:focus,
.editable select:focus {
  outline: none;
  border-color: #4C6EF5;
}

.action-buttons {
  display: flex;
  gap: 8px;
}

.action-btn {
  padding: 4px 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
  color: #666;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s;
}

.action-btn:hover {
  background: #f8f9fa;
}

.action-btn.save {
  background: #4C6EF5;
  color: white;
  border-color: #4C6EF5;
}

.action-btn.delete {
  background: #868e96;
  color: white;
  border-color: #868e96;
}

.action-btn.cancel {
  background: #868e96;
  color: white;
  border-color: #868e96;
}

/* 수정 모드의 입력 필드 스타일 */
input, select {
  width: auto;
  min-width: 80px;
  max-width: 120px;
  padding: 4px 8px;
  border: 1px solid #e9ecef;
  border-radius: 4px;
  font-size: inherit;
  font-family: inherit;
  color: inherit;
  background: #f8f9fa;
  margin: 0;
  line-height: inherit;
}

/* 숫자 입력 필드 */
input[type="number"] {
  text-align: right;
  padding-right: 20px;
}

/* 메모 입력 필드 */
input[type="text"] {
  width: 100%;
  max-width: 200px;
}

/* 카테고리 선택 필드 */
select {
  padding-right: 24px;
  background-position: right 4px center;
}

/* 포커스 스타일 */
input:focus,
select:focus {
  outline: none;
  border-color: #4C6EF5;
  background: white;
  box-shadow: none;
}

/* 수정/취소 버튼 */
.action-btn {
  padding: 2px 8px;
  font-size: 11px;
  border-radius: 4px;
}
</style>
<template>
  <div class="write-modal">
    <div class="modal-header">
      <h3>11월 2일 가계부 작성</h3>
      <button class="close-btn">×</button>
    </div>

    <div class="amount-input">
      <span>0원</span>
      <button class="edit-btn">✎</button>
    </div>

    <div class="type-selector">
      <button class="type-btn" :class="{ active: type === 'expense' }">지출</button>
      <button class="type-btn" :class="{ active: type === 'income' }">수입</button>
    </div>

    <div class="form-group">
      <div class="form-item">
        <label>분류</label>
        <select>
          <option value="">선택</option>
        </select>
      </div>

      <div class="form-item">
        <label>카테고리</label>
        <select>
          <option value="">선택</option>
        </select>
      </div>

      <div class="form-item">
        <label>결제 수단</label>
        <select>
          <option value="">선택</option>
        </select>
      </div>

      <div class="form-item">
        <label>가게명</label>
        <input type="text" placeholder="입력해주세요">
      </div>

      <div class="form-item">
        <label>메모</label>
        <input type="text" placeholder="입력해주세요">
      </div>
    </div>

    <div class="add-account">
      <button class="add-btn">
        <span>다른 가계부 내역에 추가</span>
        <span class="plus">+</span>
      </button>
    </div>

    <button class="submit-btn">작성 완료</button>
  </div>
</template>

<style scoped>
.write-modal {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  width: 280px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.modal-header h3 {
  font-size: 16px;
  font-weight: 600;
  color: #1a1438;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 20px;
  color: #666;
  cursor: pointer;
}

.amount-input {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 16px;
}

.amount-input span {
  font-size: 16px;
  font-weight: 500;
}

.edit-btn {
  background: none;
  border: none;
  color: #666;
  cursor: pointer;
}

.type-selector {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
}

.type-btn {
  flex: 1;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
}

.type-btn.active {
  background: #4C6EF5;
  color: white;
  border-color: #4C6EF5;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}

.form-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.form-item label {
  font-size: 14px;
  color: #666;
}

.form-item select,
.form-item input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.add-account {
  margin-bottom: 16px;
}

.add-btn {
  width: 100%;
  padding: 12px;
  background: #f8f9fa;
  border: none;
  border-radius: 8px;
  color: #4C6EF5;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
}

.plus {
  font-size: 16px;
}
</style>
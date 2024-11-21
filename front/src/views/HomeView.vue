<script setup>
import { ref } from 'vue';
import axios from 'axios';

const selectedImage = ref(null)

const handleFileUpload = function (event) {
  selectedImage.value = event.target.files[0]
  console.log(selectedImage.value)
}

const uploadImage = async function () {
  const formData = new FormData()
  formData.append('image',selectedImage.value)
  console.log(formData)

  try {
    const response = await axios.post(' http://127.0.0.1:8000/account/books/receipt/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Token 15442ecff0a2514893e9fad94abc373f676e968e',  // CSRF 토큰을 헤더에 추가
      }
    });
    console.log('Upload success:', response.data);
  } catch (error) {
    console.error('Upload error:', error);
  }
}


</script>

<template>

<label for="image">영수증 넣기</label>
  <input type="file" id="image" name="image" accept="image/png, image/jpeg, image.jpg" @change="handleFileUpload"/>
  <button @click="uploadImage">영수증 업로드</button>

</template>

<style scoped>

</style>
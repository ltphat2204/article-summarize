<template>
  <div class="container home">
    <h1 class="title">Tool tóm tắt tin tức</h1>
    <form class="search-wrap" @submit.prevent="handleFetch">
      <input
        name="search"
        id="search"
        v-model="search"
        placeholder="Các từ khóa được phân cách bởi dấu phẩy ,"
      />
      <SearchIcon />
    </form>
    <div class="search-content">
      <LoadingDots v-if="loading" />
      <div v-else-if="data.length && wordcloud">
        <div class="result-section">
          <h5 class="description">Wordcloud các keywords phổ biến</h5>
          <img class="wordcloud" :src="wordcloud" alt="Wordcloud" />
        </div>
        <div class="result-section">
          <h5 class="description">Có {{ data.length }} bài viết phù hợp trong vòng 24 giờ qua</h5>
          <ArticleRow
            v-for="(article, index) in data"
            :key="index"
            :title="article.title"
            :source="article.source"
            :time="article.time"
            :description="article.description"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import SearchIcon from './components/icons/SearchIcon.vue';
import LoadingDots from './components/LoadingComponent.vue';
import ArticleRow from './components/ArticleRow.vue';

const search = ref('');
const loading = ref(false);
const data = ref([]);
const wordcloud = ref('');

const tokenizeText = (text) => text.split(',').map((value) => value.trim());

const handleFetch = async () => {
  if (search.value.trim() === '') return;

  data.value = [];
  wordcloud.value = '';

  const req = {
    search: tokenizeText(search.value),
  };

  loading.value = true;

  try {
    const res = await fetch(`http://localhost:5000/crawl`, {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(req),
    });
    const result = await res.json();
    if (result.detail) {
      alert(result.detail);
      loading.value = false;
    } else {
      data.value = result;
      getWordcloud();
    }
  } catch (err) {
    alert(err);
    loading.value = false; 
  }
};

const getWordcloud = async () => {
  const req = {
    text: data.value.map((value) => value.description).join(' '),
  };

  try {
    const res = await fetch(`http://localhost:5000/wordcloud`, {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(req),
    });
    const blob = await res.blob();
    wordcloud.value = URL.createObjectURL(blob);
    loading.value = false;
  } catch (err) {
    console.log(err);
    loading.value = false;
  }
};
</script>
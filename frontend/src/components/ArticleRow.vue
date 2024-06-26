<template>
  <div class="article-row">
    <a :href="props.source" target="_blank" rel="noopener noreferrer" class="article-title">{{ props.title }}</a>
    <div class="article-time">{{ props.time }}</div>
    <div class="article-description">{{ props.description }}</div>
  </div>
</template>

<script setup>
const props = defineProps({
  title: String,
  source: String,
  time: String,
  description: String,
});
</script>
  
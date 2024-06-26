<template>
  <div class="loading-dots">
    Loading {{ dots }}
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watchEffect } from 'vue';

const dots = ref('');
const increase = ref(false);

const updateDots = () => {
  if (dots.value.length === 3) {
    increase.value = false;
  }
  if (dots.value.length === 0) {
    increase.value = true;
  }
  dots.value = increase.value ? dots.value + '.' : dots.value.slice(1);
};

let intervalId;

onMounted(() => {
  intervalId = setInterval(updateDots, 300);
});

onUnmounted(() => {
  clearInterval(intervalId);
});
</script>
  
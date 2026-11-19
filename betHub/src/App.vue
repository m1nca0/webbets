<script setup lang="ts">
import {onBeforeMount, ref} from 'vue'
import axios from "axios"

const sports = ref([]);
let loading: Boolean = true;

async function fetchSports(){
  // loading = true;
  const r = await axios.get('/api/sports/');
  sports.value = r.data;
  console.log(r.data)
  // loading = false;

}

async function onLoadCLick() {
  await fetchSports()
}

onBeforeMount(async () => {
  await fetchSports()
})
</script>

<template>
<div v-for="item in sports">
    {{ item.name }}
</div>
</template>

<style scoped>

</style>

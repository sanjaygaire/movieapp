<script setup>
import { ref , reactive, computed} from 'vue'

const  initialState= reactive({val:{count:0},user:['sanjay','elis']})
const user= ref('')
const a = ref(5)
const b=ref(30)
const c= computed(()=>a.value+b.value)
</script>

<template>
<h1>
  count:{{ initialState.val.count }}
</h1>
<button @click="initialState.val.count++">+</button>
<button @click="initialState.val.count--">-</button>
<p>
  this is created by {{ initialState.user}}
</p>
{{ user }}
<button @click="user='sanjay'">
  Add user
</button>

<h1>
   {{ c }}
</h1>

</template>

<style scoped>

</style>

<template>
  <div>
    <h1> {{ this.$route.meta.title }} </h1>
    <div v-if="posts && posts.length">
        Студент записан на курс: {{posts}}
    </div>
    <div v-else>
        Не выбран курс на странице <a href="/">Home</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      posts: [],
      errors: []
    }
  },

  // Fetches posts when the component is created.
  created() {
    let url_normalized = this.$route.query.url
    
    axios.get(url_normalized.replace("http://127.0.0.1/", 'http://127.0.0.1:8000/'))
    .then(response => {
      // JSON responses are automatically parsed.
      this.posts = response.data.name
      console.log(this.posts)
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}

</script>

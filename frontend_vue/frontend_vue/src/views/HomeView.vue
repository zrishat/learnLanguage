<template>
  <div>
    <h1> {{ this.$route.meta.title }} </h1>
    <div v-if="posts && posts.length">
      <p v-for="post of posts" :key="post">
            <router-link :to="{path: 'info-course', query: {url:post.url}}">
                {{post.name}}
            </router-link>
      </p>
    </div>

    <ul v-if="errors && errors.length">
      <li v-for="error of errors" :key="error">
        {{error.message}}
      </li>
    </ul>
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
    axios.get(`http://127.0.0.1:8000/drf/courses/`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.posts = response.data.results
      //console.log(this.posts)
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}

</script>
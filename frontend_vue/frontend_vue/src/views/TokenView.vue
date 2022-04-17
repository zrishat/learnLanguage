<template>
    <div>
        <h1> {{ this.$route.meta.title }} </h1>
        <p>Токен для пользователя admin: {{ token }}</p>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      token: "",
      errors: []
    }
  },

  // Fetches posts when the component is created.
  created() {
    axios.post(`http://127.0.0.1:8000/api-token-auth/`, {
        'username': 'admin',
        'password': 'admin'
    })
    .then(response => {
      // JSON responses are automatically parsed.
      this.token = response.data.token
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}

</script>
// fetch example, get users if already logged by admin
fetch('http://127.0.0.1:8000/drf/users/?format=json')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log('fetch example', data);
  });


import axios from 'axios'
// axios example add new group
axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/drf/groups/',
    data: {
      name: 'NewGroup123',
    }
  });
  
<template>
    <div>
        <b-table striped hover :items="items" :fields="fields"></b-table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data () {
      return {
        fields: ['id','title','score','readed'],
        items: [],
      }
    },
    created() {
    axios
      .get('http://localhost:5000/books')
      .then((res) => {
        this.items = res.data
      })
    }
}
</script>
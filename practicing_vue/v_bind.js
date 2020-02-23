Vue.component('cat-list', {
    props: ['cats'],
    template: 
    '<ul> <li v-for="cat in cats">{{ cat.name }}</li> </ul>'
})

new Vue({
    el: '#root', //locate the container id for the application
    component: [
        'cat-list'
    ],
    data: {
      email: 'email@email.com',
      cats: [
        { name: 'cat1'},
        { name: 'cat2'},
        { name: 'cat3'},
      ],
      newCat: ''
    },
    methods: {
        addKitty: function() {
            this.cats.push({name: this.newCat})
            this.newCat = ''
        },
    },
    filters: {
        //receive a value and return to upperCase
        capitalize: function(value) {
            return value.toUpperCase()
        }
    },
    computed: {
        kittyfyName: function () {
            if (this.newCat.length > 1) {
                return this.newCat + 'y'
            }
        }
    }
  });
  
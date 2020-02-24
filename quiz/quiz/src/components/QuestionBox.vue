<template>
  <div class="quetion-box-container">
    <b-jumbotron>
      <template v-slot:lead>
        {{ currentQuestion.question }}
      </template>
      <hr class="my-4">

      <b-list-group>
        <b-list-group-item 
          v-for="(answer, index) in answers" 
          v-bind:key="index"
          v-on:click="selectAnswer(index)"
          v-bind:class="[selectedIndex === index ? 'selected': '']">
          {{ answer }}
        </b-list-group-item>
      </b-list-group>
      <b-button variant="primary" 
        v-on:click="submitAnswer"
        href="#">Submit</b-button>
      <b-button v-on:click="next" variant="success" href="#">Next</b-button>
    </b-jumbotron>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  props: {
    currentQuestion: Object,
    next: Function,
    increment: Function
  },
  data () {
    return {
      selectedIndex: null,
      shuffedAnswers: []
    }
  },
  methods: {
    selectAnswer: function (index) {
      this.selectedIndex = index;
      console.log(index);
    },
    shuffleAnswers () {
      let answers = [...this.currentQuestion.incorrect_answers, this.currentQuestion.currectQuestion];
      this.shuffedAnswers = _.shuffle(answers)
    },
    submitAnswer() {
      let isCorrect = false
      if (this.selectedIndex === this.correctIndex){
        isCorrect = true
      }

      this.increment(isCorrect)
    }
  },
  watch: {
    currentQuestion: {
      immediate: true,
      handler() {
        this.selectedIndex = null
        this.shuffleAnswers()
      }
    },
  },
  computed: {
    answers() {
      let answers = [...this.currentQuestion.incorrect_answers];
      answers.push(this.currentQuestion.correct_answer);
      return answers
    }
  },
  mounted() {
    this.shuffleAnswers()
  }
}
//style scoped means that this style is local, onle for this template, not for all elements
</script>

<style scoped>
.list-group {
  margin-bottom: 15px;
}
.list-group-item:hover {
  background: #EEE;
  cursor: pointer;
}
.btn {
  margin: 0 5px;
}

.selected {
  background-color: lightblue;
}

.correct {
  background-color: lightgreen;
}

.incorrect {
  background-color: lightred;
}
</style>

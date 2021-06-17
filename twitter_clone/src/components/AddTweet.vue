<template>
  <form class="form__container" @submit.prevent="onSubmit">
    <label>What's on your mind?</label>
    <textarea v-model="state.message" cols="30" rows="10"></textarea>
    <label>name</label>
    <input v-model="state.name" type="text" />
    <button>Submit</button>
  </form>
</template>

<script>
import { reactive } from "vue";

//Add.vue (Parent) >> call >> AddTweet.vue(Childent)
export default {
//Composition API****
  //generate vue - instant
    setup(props, ctx) { //ctx == context >> &emit to parent
    const state = reactive({
        message: '',
        name: '',
        url: '',
    });

    function onSubmit () {
        ctx.emit('form-submit',{ //ctx == context >> &emit to parent
        message: state.message,
        name : state.name,
        url : state.url}
        );
        state.message = '';
        state.name = '';
        state.url = '';
    }

    return { state, onSubmit };
  }

//Optional API****
  // data () {
  //     return {
  //         message : "",
  //         name : "",
  //         url : ""
  //     };
  // },
  // methods: { //sent data() to parent and submit at parent ; used $emit
  //     onSubmit (){
  //         this.$emit('form-submit',{
  //         message: this.message,
  //         name : this.name,
  //         url : this.url}
  //         );
  //         //(name_event_string,{data}) ;form-submit ส่งไป component parent ที่สูงกว่า
  //         this.message = '';
  //         this.name = '';
  //         this.url = '';
  //         //reset form
  //     }
  // }
};
</script>

<style>
</style>
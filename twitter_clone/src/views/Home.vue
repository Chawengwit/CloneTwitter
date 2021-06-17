<template>
  <div>
    <AddTweet @form-submit="onSubmit" />
    <Tweet
      v-for="(post, index) in state.posts"
      :key="index"
      :message="post.message"
      :name="post.name"
      :url="post.url"
    />
  </div>
</template>

<script>
//Binding Methods >> inject to HTML tag ; used > :prop_child='val_parent'
import AddTweet from "../components/AddTweet.vue";
import Tweet from "../components/Tweet.vue";

//create variable data****
import { reactive } from "vue";

export default {
  name: "App",
  components: { AddTweet, Tweet },
//Composition API in function setup****
  setup() {
    const state = reactive({  //data
      posts: [],
    });

    async function created() { //created
      const res = await fetch("/post");
      const resJson = await res.json();

      state.posts = resJson.posts;
    }
    created();

    async function onSubmit(val) { //method
      state.posts.push(val);
      const res = await fetch("/post", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(val),
      });

      const resJson = await res.json();
      console.log(resJson);
    }

    return { state, onSubmit }; //created ไม่ต้อง return เพราะไม่ได้ใช้แสดงในหน้าเว็บ
  },
//Optional normal REST API****
  // data() {
  //   //Binding
  //   return {
  //     posts: [],
  //   };
  // },
  //   async created() {
  //     const res = await fetch("/post");
  //     const resJson = await res.json();

  //     this.posts = resJson.posts;
  //   },
  // // Using Fetch Function(RES API)-----
  // methods: {
  //   //used fetch function(end API route, option; method, header, body) call backend
  //   async onSubmit(val) {
  //     this.posts.push(val);
  //     const res = await fetch("/post", {
  //       //url end point ; 1. shoot val to post
  //       method: "POST", //method ; 2. next shoot to 'POST'
  //       headers: {
  //         //define content type
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify(val), // body string >> json
  //     });

  //     const resJson = await res.json();
  //     console.log(resJson)

  //   },
  // },
};
</script>




<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.form__container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>

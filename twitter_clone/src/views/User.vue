<template>
  <router-link to="/">Home</router-link>
    <Tweet
      v-for="(post, index) in state.posts"
      :key="index"
      :message="post.message"
      :name="post.name"
      :url="post.url"
    />
</template>

<script>
import Tweet from "../components/Tweet.vue";
import { reactive } from "vue";

export default {
  props : {
    name : String
  },
  // props : ["name"],
  components: { Tweet },
  setup (props){
    const state = reactive ({
      posts: []
    });
    async function created() {
      const res = await fetch(`/post?user=${props.name}`);
      const resJson = await res.json();

      state.posts = resJson.posts;

      console.log(state.posts);
    }
    created();

    return { state };
  },
    // props: ["name"],
    // components: { Tweet },
    // data() {
    //     return {
    //     posts: [],
    //     };
    // },
    // async created() {
    // const res = await fetch(`/post?user=${this.name}`);
    // const resJson = await res.json();

    // this.posts = resJson.posts;
    // },
};

</script>

<style>
</style>
<template>
    <div class="tweet">
        <div class="tweet_img_container">
            <!-- .ใส่ : เพื่อ bind -->
            <a :href="url"></a>   
            <img
                :src="url"
                alt=""
                style="width: 96px; height:96px;"
            />
        </div>
        <div class="tweet_text_container">
            <p class="tweet_text">
                {{ message }}
            </p>
            <p>Posted by: <router-link :to='{ name: "User", params: {name} }'>{{ name }}</router-link></p>
        </div>
    </div>
    
</template>

<script>
export default {
    props: [ //like a data(but immuted)
        'message', 'name', 'url' //defind value by parent to message and name
        //and next to used
    ]
}
</script>

<style>
.tweet {
    display: flex;
    width: 90%;
    margin: 0.5rem 1rem;
    padding: 1rem;
    border-style: solid;
    border-width: 0.05rem;
    border-color: black;
    border-radius: 1rem;
    justify-content: space-around;
}

.tweet_img_container{
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
}

.tweet_text_container{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex: 3;
}

.tweet_author{
    font-weight: bold;
}

.tweet_text{
    font-size: 1.1rem;
    text-align: start;
}
</style>
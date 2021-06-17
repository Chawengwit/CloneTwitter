module.exports = {
    devServer: {
        proxy: {
            "/post":{
                target:'http://127.0.0.1:5000/'
            },
        },
    },
};
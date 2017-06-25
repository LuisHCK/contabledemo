//Inialize Vue app
var app = new Vue({
    delimiters: ['<%', '%>'],
    el: '#app',
    data: {
        accounts: []
    },
    mounted() {
        axios.get("/accounts").then(
            response => {
                this.accounts = response.data;
                console.log(this.accounts)
            }
        )
    }
})
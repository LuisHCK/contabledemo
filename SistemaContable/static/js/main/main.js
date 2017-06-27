//Inialize Vue app
var app = new Vue({
    delimiters: ['<%', '%>'],
    el: '#app',
    data: {
        accounts: [],
        categories: [],

        //Temporally store new account data
        newAccount:{
            AccountID:'',
            AccountName: '',
            CategoryID: ''
        }
    },
    mounted() {
        axios.get("/accounts")
            .then(
                response => {
                    this.accounts = response.data;
                    console.log(this.accounts)
                })
            .catch(function (error) {
                console.log(error);
            });
        axios.get("/accounts/categories")
            .then(
                response => {
                    this.categories = response.data;
                })
            .catch(function (error) {
                console.log(error);
            });
    },
    updated() {
        $('.collapsible').collapsible();
        $('select').material_select();
    },
    methods: {
        addAccount: function() {
            axios.post($("#form_account").attr('action'), {
                    name: this.newAccount.AccountName, // get the data from v-models
                    category_id: this.newAccount.CategoryID
                })
                .then(function (response) {
                    console.log(response.data)
                    app.newAccount.AccountID = response.data['id'] //Sets the id to given by backend
                    app.accounts.push(app.newAccount) // put on Vue data
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    }
});
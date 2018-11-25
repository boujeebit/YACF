import { api } from '@/utils/api.js'
import store from '@/store/index'

export function graud (to, from, next) {
    api('query{ me { id, isSuperuser, username, firstName, lastName, profile{ team { name } } } }').then(data => {
        console.log(data)
        if(data.me !== null) {
            console.log("Should login: ", data.me);
            store.state.user.user = data.me
            store.state.user.auth = true
            next();
        } else {
            console.log("[ROUTE]: Authenication failed, going to login")
            next('/login');
        }
    })
}
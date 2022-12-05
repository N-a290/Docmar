import { createWebHistory, createRouter } from "vue-router";
import Home from "../components/Home.vue";
import Contact from "../components/Contact.vue";
import Search from "../components/Search.vue";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
  },
  {
    path: "/search",
    name: "Search",
    component: Search,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
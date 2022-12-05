<template>
    <div class="row">
        <!-- SIDE NAVIGATION -->
        <aside class="col-lg-2 my-4">
            <div class="d-none d-lg-block ">
                <ul class="nav flex-column nav-pills menu-sidebar ps" data-mdb-allow-hashes="true"
                    style="max-height: 620px;">

                    <li class="nav-item">
                        <a class="nav-link">Libros</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Revistas</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Iconográficos</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Monografías</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Ensayos</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Investigaciones</a>
                    </li>
                    <li>
                        <hr>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Electrónicos</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Físicos</a>
                    </li>

                    <div class="ps__rail-y" style="top: 0px; right: 0px; opacity: 1; height: 276px;">
                        <div class="ps__thumb-y" tabindex="0" style="top: 0px; height: 0px;"></div>
                    </div>
                </ul>
            </div>
        </aside>
        <div class="col-lg-10 col-md-12">
            <h1 class="display-1">Resultados de tu busqueda</h1>
            <div class="row" v-for="document in data" v-bind:key="document._id">
                <div class="col">
                    <figure class="mb-4">
                        <img :src="document.get_image">
                    </figure>

                    <h3>{{document.title}}</h3>
                    <p>{{document.summary}}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import axios from 'axios'

export default {
    name: 'search',
    // data() {
    //     return {
    //         data: []
    //     }
    // },
    // mounted(){
    //     this.getData()
    // },
    // methods: {
    //     getData(){

    //     }
    // }
}
</script>

<style scoped>
aside {
    background-color: #EC9F05;
}

a {
    color: black;
}

a:hover {
    color: #D76A03;
}
</style>
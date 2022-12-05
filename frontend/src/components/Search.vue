<template>
    <div class="row">
        <aside class="col-lg-2 my-4">
            <div class="d-none d-lg-block ">
                <ul class="nav flex-column nav-pills menu-sidebar ps" data-mdb-allow-hashes="true"
                    style="max-height: 620px;">


                    <li class="nav-item">
                        <a class="nav-link">Introduction</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Basic example</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Positioning</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Colors</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Dark</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Inner scroll</a>
                    </li>

                    <div class="ps__rail-x" style="left: 0px; bottom: 0px;">
                        <div class="ps__thumb-x" tabindex="0" style="left: 0px; width: 0px;"></div>
                    </div>
                    <div class="ps__rail-y" style="top: 0px; right: 0px; opacity: 1; height: 276px;">
                        <div class="ps__thumb-y" tabindex="0" style="top: 0px; height: 0px;"></div>
                    </div>
                </ul>
            </div>
        </aside>
        <div class="col-lg-10 col-md-12">
            <h1 class="display-1">Resultados de tu busqueda</h1>
        </div>
    </div>
</template>

<script>
export default {
    name: 'search'
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
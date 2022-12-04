<script setup>
</script>

<template>
  <div>

    <!-- NAVEGACION -->
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <img src="./assets/library-icon.svg" alt="library-icon" width="40" height="30"
            class="d-inline-block align-text-bottom">
          Docmar
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mr-2 mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link active" to="/contact">Acerca de</router-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                Documentos
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Revistas</a></li>
                <li><a class="dropdown-item" href="#">Iconográficos</a></li>
                <li><a class="dropdown-item" href="#">Monografías</a></li>
                <li><a class="dropdown-item" href="#">Ensayos</a></li>
                <li><a class="dropdown-item" href="#">Investigaciones</a></li>
                <li>
                  <hr class="dropdown-divider">
                </li>
                <li><a class="dropdown-item" href="#">Electrónicos</a></li>
                <li><a class="dropdown-item" href="#">Físicos</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/">Registarse | Ingresar</router-link>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Buscar">
            <button class="btn btn-outline-success" type="submit">Buscar</button>
          </form>
        </div>
      </div>
    </nav>
    <!-- FIN DE LA NAVEGACION -->

    <!-- CONTENIDO -->
    <router-view />

    <!-- FOOTER -->
    <footer>
      <div class="container p-3">
        <div class="row text-center text-white">
          <div class="col ml-auto">
            <p>Hecho con Vue | 2022</p>
          </div>
        </div>
      </div>
    </footer>
    <!-- FIN DEL FOOTER -->
  </div>
</template>

<style scoped>
.navbar {
  box-shadow: 2px 2px 5px #000;
  opacity: 0.9;
}

footer {
  background: #BF3100;
}
</style>

<template>

    <!-- HEADER -->
    <header class="main-header">
        <div class="background-overlay text-white py-5">
            <div class="container">
                <div class="row d-flex h-100">
                    <div class="col-sm-6 text-center justify-content-center align-self-center">
                        <h1>
                            El principito
                        </h1>
                        <p>Encontraras muchos libros y muchos mas documentos.</p>
                        <a href="#" class="btn btn-outline-secondary btn-lg text-white">
                            Leer mas
                        </a>
                    </div>
                    <div class="col-sm-6">
                        <img src="../assets/product.jpg" class="img-fluid d-none d-sm-block" style="width: 80%">
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- NEWSLETTER  -->
    <section id="newsletter" class="bg-dark text-white py-5">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <input type="text" class="form-control form-control-lg" placeholder="Introduzca su nombre">
                </div>
                <div class="col-md-4">
                    <input type="email" class="form-control form-control-lg" placeholder="Introduzca su Email">
                </div>
                <div class="col-md-4">
                    <button class="btn btn-success btn-lg btn-block">
                        Suscribir
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- FEATURES -->

    <section class="py-5">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <div class="card text-center border-success">
                        <div class="card-body">
                            <h3>Caracteristica 1</h3>
                            <p>
                                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Doloribus, voluptatum?
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-white bg-success">
                        <div class="card-body">
                            <h3>Caracteristica 2</h3>
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi, eaque.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-center border-success">
                        <div class="card-body">
                            <h3>Caracteristica 3</h3>
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum, incidunt?
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-center border-success">
                        <div class="card-body">
                            <h3>Caracteristica 4</h3>
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae, laborum.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ABOUT -->
    <section class="m5 text-center bg-light">
        <div class="container">
            <div class="row">
                <div class="m-5">
                    <h3 class="text-center">¿Por qué este producto?</h3>
                    <p>
                        El principito es una novela corta y la obra más famosa del escritor y aviador francés Antoine de
                        Saint-Exupéry.
                    </p>
                </div>
            </div>
        </div>
    </section>

</template>

<script>
export default {
    name: 'home'
}

</script>

<style scoped>
.main-header {
    position: relative;
    background-size: cover;
    min-height: 700px;
}

.background-overlay {
    background: #EC9F05;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

</style>
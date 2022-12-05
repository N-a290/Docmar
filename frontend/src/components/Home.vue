<template>

    <!-- HEADER -->
    <header class="main-header">
        <div class="background-overlay text-white py-5">
            <div class="container">
                <div class="row d-flex h-100">
                    <div class="col-sm-6 text-center justify-content-center align-self-center">
                        <h1>
                            Bienvenido
                        </h1>
                        <p>Docmar.com es un punto de encuentro entre autores y lectores en el que tu participación es una pieza muy importante.</p>
                        <a href="/contact" class="btn btn-outline-secondary btn-lg text-white">
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
            <h2>Suscríbase para estar al tanto de nuestras ofertas</h2>
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
                            <h3>Fácil de usar</h3>
                            <p>
                                Si recibiste un producto defectuoso o no era el acordado, nunca perderás tu dinero. Te acompañamos hasta que estés conforme con lo que compraste.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-white bg-success">
                        <div class="card-body">
                            <h3>Seguro</h3>
                            <p>
                                Todas tus compras están fuertemente aseguradas, y nuestro servicio al cliente siempre está dispuesto a solucionara cualquier duda que se te presente
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-center border-success">
                        <div class="card-body">
                            <h3>Rapidez</h3>
                            <p>
                                Tus pedidos serán entregados con agilidad y rapidez, realizamos entregas por toda Colombia
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-center border-success">
                        <div class="card-body">
                            <h3>Paga con tarjeta o con efectivo</h3>
                            <p>
                                Paga en cuotas y aprovecha la comodidad de financiación que te da tu banco, o hazlo con efectivo en puntos de pago. ¡Y siempre es seguro!
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ABOUT -->
    <section class=" text-center bg-light">
        <div class="container">
            <div class="row">
                <div class="m-5">
                    <h3 class="">¿Nuestra misión?</h3>
                    <p>
                        Utilizar el poder de la tecnología emergente para hacer que todos los documentos sean más accesibles y baratos para todos, de modo que un día todas las personas del mundo tengan fácil acceso al mundo literario y académico.
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
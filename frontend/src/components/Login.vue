<template>
    <section class="w-100 p-4 d-flex justify-content-center pb-4">
        <div class="login">
            <h1 class="m-4 text-center">Iniciar Sesión</h1>
            <form>
                <!-- Email input -->
                <div class="form-outline mb-4">
                    <input type="email" id="formField1" class="form-control" />
                    <label class="form-label" for="formField1">Correo electrónico</label>
                </div>

                <!-- Password input -->
                <div class="form-outline mb-4">
                    <input type="password" id="formField2" class="form-control" />
                    <label class="form-label" for="formField2">Contraseña</label>
                </div>

                <!-- 2 column grid layout for inline styling -->
                <div class="row mb-4">
                    <div class="col d-flex justify-content-center">
                        <!-- Checkbox -->
                        <div class="form-check">
                            <input class="form-check-input bg-success" type="checkbox" value="" id="formField31" checked />
                            <label class="form-check-label" for="formField31">Recordarme</label>
                        </div>
                    </div>

                    <div class="col">
                        <!-- Simple link -->
                        <a href="#!">Olvidaste tu contraseña?</a>
                    </div>
                </div>

                <!-- Submit button -->
                <button type="button" class="btn btn-success btn-block mb-4">Iniciar sesión</button>

                <!-- Register buttons -->
                <div class="text-center">
                    <p>No tienes cuenta? <a href="/register">Regístrate</a></p>
                    <p>o inicia sesión con:</p>
                    <button type="button" class="btn btn-outline-success btn-floating mx-1">
                        <i class="fab fa-facebook-f"></i>
                    </button>

                    <button type="button" class="btn btn-outline-success btn-floating mx-1">
                        <i class="fab fa-google"></i>
                    </button>

                    <button type="button" class="btn btn-outline-success btn-floating mx-1">
                        <i class="fab fa-twitter"></i>
                    </button>

                    <button type="button" class="btn btn-outline-success btn-floating mx-1">
                        <i class="fab fa-github"></i>
                    </button>
                </div>
            </form>
        </div>
    </section>
</template>

<script>
export default {
    name: 'login'
}

</script>

<style scoped>
.login {
    width: 28rem;
}
</style>
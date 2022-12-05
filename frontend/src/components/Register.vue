<template>
    <section class="w-100 p-4 d-flex justify-content-center pb-4">
        <div class="login">
            <h1 class="m-4 text-center">Registarse</h1>
            <form>
                <div class="text-center mb-3">
                    <p>Sign up with:</p>
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

                <p class="text-center">or:</p>

                <!-- Name input -->
                <div class="form-outline mb-4">
                    <input type="text" id="registerName" class="form-control">
                    <label class="form-label" for="registerName" style="margin-left: 0px;">Nombre</label>
                    <div class="form-notch">
                        <div class="form-notch-leading" style="width: 9px;"></div>
                        <div class="form-notch-middle" style="width: 42.4px;"></div>
                        <div class="form-notch-trailing"></div>
                    </div>
                </div>

                <!-- Username input -->
                <div class="form-outline mb-4">
                    <input type="text" id="registerUsername" class="form-control">
                    <label class="form-label" for="registerUsername" style="margin-left: 0px;">Nombre de usuario</label>
                    <div class="form-notch">
                        <div class="form-notch-leading" style="width: 9px;"></div>
                        <div class="form-notch-middle" style="width: 66.4px;"></div>
                        <div class="form-notch-trailing"></div>
                    </div>
                </div>

                <!-- Email input -->
                <div class="form-outline mb-4">
                    <input type="email" id="registerEmail" class="form-control">
                    <label class="form-label" for="registerEmail" style="margin-left: 0px;">Correo electrónico</label>
                    <div class="form-notch">
                        <div class="form-notch-leading" style="width: 9px;"></div>
                        <div class="form-notch-middle" style="width: 40px;"></div>
                        <div class="form-notch-trailing"></div>
                    </div>
                </div>

                <!-- Password input -->
                <div class="form-outline mb-4">
                    <input type="password" id="registerPassword" class="form-control">
                    <label class="form-label" for="registerPassword" style="margin-left: 0px;">Contraseña</label>
                    <div class="form-notch">
                        <div class="form-notch-leading" style="width: 9px;"></div>
                        <div class="form-notch-middle" style="width: 64.8px;"></div>
                        <div class="form-notch-trailing"></div>
                    </div>
                </div>

                <!-- Repeat Password input -->
                <div class="form-outline mb-4">
                    <input type="password" id="registerRepeatPassword" class="form-control">
                    <label class="form-label" for="registerRepeatPassword" style="margin-left: 0px;">Repite la
                        contraseña</label>
                    <div class="form-notch">
                        <div class="form-notch-leading" style="width: 9px;"></div>
                        <div class="form-notch-middle" style="width: 106.4px;"></div>
                        <div class="form-notch-trailing"></div>
                    </div>
                </div>

                <!-- Checkbox -->
                <div class="form-check d-flex justify-content-center mb-4">
                    <input class="form-check-input me-2 bg-success" type="checkbox" value="" id="registerCheck" checked=""
                        aria-describedby="registerCheckHelpText">
                    <label class="form-check-label" for="registerCheck">
                        Estoy deacuerdo con los términos y condiciones
                    </label>
                </div>

                <!-- Submit button -->
                <button type="submit" class="btn btn-success btn-block mb-3">Registarse</button>
            </form>
        </div>
    </section>
</template>

<script>
export default {
    name: 'register'
}

</script>

<style scoped>
.login {
    width: 28rem;
}
</style>
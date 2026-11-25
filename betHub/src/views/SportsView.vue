<script setup lang="ts">
import { onBeforeMount, ref } from "vue";
import axios from "axios";
import Cookies from "js-cookie";

onBeforeMount(() => {
  axios.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");
});

type SportType = "team" | "individual" | "pair";

interface Sport {
  id: number;
  name: string;
  type: SportType;
}

const sportToAdd = ref<{ name: string; type: SportType }>({
  name: "",
  type: "team",
});
const sportToEdit = ref<{ name: string; type: SportType }>({
  name: "",
  type: "team",
});
const sports = ref<Sport[]>([]);

const sportsTypeList = ref([
  { value: "team", name: "Командный" },
  { value: "individual", name: "Индивидуальный" },
  { value: "pair", name: "Парный" },
]);

async function fetchSports() {
  const r = await axios.get("/api/sports/");
  sports.value = r.data;
  console.log(r.data);
}

async function onSportsToAdd() {
  await axios.post("/api/sports/", {
    ...sportToAdd.value,
  });
  await fetchSports();
}
async function onRemoveClick(sports: Sport) {
  await axios.delete(`/api/sports/${sports.id}/`);
  await fetchSports();
}

async function onSportEditClick(sport: Sport) {
  sportToEdit.value = { ...sport };
}

async function onUpdateSport() {
  await axios.put(`/api/sports/${sportToEdit.value.id}/`, {
    ...sportToEdit.value,
  });
  await fetchSports();
}

onBeforeMount(async () => {
  await fetchSports();
});
</script>

<template>
  <form @submit.prevent.stop="onSportsToAdd">
    <div class="row">
      <div class="col">
        <div class="form-floating">
          <input
            type="text"
            class="form-control"
            v-model="sportToAdd.name"
            required
          />
          <label for="floatingInput">Спорт</label>
        </div>
      </div>
      <div class="col-auto">
        <div class="form-floating">
          <select class="form-select" v-model="sportToAdd.type" required>
            <option :value="t.value" v-for="t in sportsTypeList">
              {{ t.name }}
            </option>
          </select>
          <label for="floatingInput">Тип</label>
        </div>
      </div>
      <div class="col-auto">
        <button class="btn btn-primary">Добавить</button>
      </div>
    </div>
  </form>

  <div v-for="item in sports" class="sport-item">
    <div>{{ item.name }}</div>
    <div>{{ item.type }}</div>
    <button
      class="btn btn-success"
      @click="onSportEditClick(item)"
      data-bs-toggle="modal"
      data-bs-target="#editSportsModal"
    >
      <i class="bi bi-pen-fill"></i>
    </button>
    <button class="btn btn-danger" @click="onRemoveClick(item)">
      <i class="bi bi-x"></i>
    </button>
  </div>

  <div class="modal fade" id="editSportsModal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Редактировать</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col">
              <div class="form-floating">
                <input
                  type="text"
                  class="form-control"
                  v-model="sportToEdit.name"
                />
                <label for="floatingInput">Фио</label>
              </div>
            </div>
            <div class="col-auto">
              <div class="form-floating">
                <select class="form-select" v-model="sportToEdit.type">
                  <option :value="t.value" v-for="t in sportsTypeList">
                    {{ t.name }}
                  </option>
                </select>
                <label for="floatingInput">Тип</label>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Закрыть
          </button>
          <button
            data-bs-dismiss="modal"
            type="button"
            class="btn btn-primary"
            @click="onUpdateSport"
          >
            Сохранить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>

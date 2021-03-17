<template>
  <div class="home">
    <h1 class="title">
      Values and the Principles of Agile Software Development.
    </h1>
    <div class="container">
      <div class="values">
        <h3>VALUES</h3>
        <div>
          <CreateValue @on-new_Value="addValues($event)" />
        </div>
        <table>
          <tbody>
            <Values
              v-for="(val, index) in values"
              :key="index.id"
              :valuesName="val.value_name"
              @on-delete_val="deleteValues(val.id)"
              @on-edit_val="editValues(val, $event)"
            />
          </tbody>
        </table>
      </div>
      <div class="principles">
        <h3>PRINCIPLES</h3>
        <div>
          <CreatePrinciple @on-new_Principle="addPrinciples($event)" />
        </div>
        <table>
          <tbody>
            <Principles
              v-for="(pri, index) in principles"
              :key="index.id"
              :principlesName="pri.principle_name"
              @on-delete_pri="deletePrinciples(pri.id)"
              @on-edit_pri="editPrinciples(pri, $event)"
            />
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Values from "../components/Values";
import Principles from "../components/Principles";
import CreateValue from "../components/CreateValue";
import CreatePrinciple from "../components/CreatePrinciple";

export default {
  components: {
    Values,
    Principles,
    CreateValue,
    CreatePrinciple,
  },
  name: "Home",
  data() {
    return {
      values: [],
      principles: [],
    };
  },
  mounted() {
    this.getValues();
    this.getPrinciples();
  },
  methods: {
    getValues() {
      axios({
        method: "GET",
        url: "http://127.0.0.1:8000/values/"

      }).then((res) => (this.values = res.data));
    },
    getPrinciples() {
      axios({
        method: "GET",
        url: "http://127.0.0.1:8000/principles/"
      })
        .then((res) => (this.principles = res.data))
        .catch((err) => console.log(err));
    },
    addValues(newValue) {
      axios.post("http://127.0.0.1:8000/values/", {
        value_name: newValue
      }).then(() => this.getValues())
    },
    addPrinciples(newPrinciple) {
      axios.post("http://127.0.0.1:8000/principles/", {
        principle_name: newPrinciple
      }).then(() => this.getPrinciples())
    },
    editValues(val, newdatavalue) {
      axios.put("http://127.0.0.1:8000/values/"+val.id+"/", {
        value_name: newdatavalue
      })
        .then((res) => console.log(res))
        .then(() => this.getValues())
    },
    editPrinciples(pri, newPrincipleString) {
            axios.put("http://127.0.0.1:8000/values/"+pri.id, {
        principle_name: newPrincipleString
      })
        .then((res) => console.log(res))
        .then(() => this.getPrinciples())
    },
    deleteValues(deleteValue) {
      axios.delete("http://127.0.0.1:8000/values/"+deleteValue)
       .then(() => this.getValues())
    },
    deletePrinciples(deletePrinciple) {
      axios.delete("http://127.0.0.1:8000/principles/"+deletePrinciple)
       .then(() => this.getPrinciples())
    },
  },
};
</script>

<style>
button {
  font-weight: bold;
  transition: 0.2s;
}
.btn-container {
  display: flex;
  justify-content: flex-end;
}
.btn-edit {
  padding: 5px;
  color: #008cba;
  background: aliceblue;
  border: 2px solid #008cba;
}
.btn-edit:hover {
  color: #fff;
  background: #008cba;
  border-radius: 6px;
}
.btn-delete {
  padding: 5px;
  color: #f44336;
  background: aliceblue;
  border: 2px solid #f44336;
}
.btn-delete:hover {
  color: #fff;
  background: #f44336;
  border-radius: 6px;
}
.btn-edit,
.btn-delete {
  margin: 3px;
}
.container {
  display: flex;
  justify-content: center;
  background-color: aliceblue;
}
h1.title,
h3 {
  display: flex;
  justify-content: center;
  color: #424242;
}
h1.title {
  color: aliceblue;
}
table {
  text-align: center;
}
tr:nth-child(even) {
  background-color: #ddd;
}
.values,
.principles {
  margin: 20px;
}
</style>

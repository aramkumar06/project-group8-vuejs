<template>
  <div id="wrapper">
    <div id="chart-area"></div>
    <div id="chart-bar"></div>

    <a class="link" href="https://apexcharts.com?ref=codepen">apexcharts.com</a>
  </div>
</template>


<script>
// Load on demand

import ApexCharts from "apexcharts";
import http from "../vuex/http-common";
export default {
  components: {},
  data() {
    return {};
  },
  methods: {
    render(list) {
      var data = [];
      console.log("*****************");
      console.log(list);

      for (let index = 0; index < list.length; index++) {
        data.push([list[index].recordDate, list[index].pointSubscriber]);
      }
      console.log(data);

      var options1 = {
        chart: {
          id: "chart2",
          type: "area",
          height: 230,
          foreColor: "#ccc",
          toolbar: {
            autoSelected: "pan",
            show: false
          }
        },
        colors: ["#00BAEC"],
        stroke: {
          width: 3
        },
        grid: {
          borderColor: "#555",
          clipMarkers: false,
          yaxis: {
            lines: {
              show: false
            }
          }
        },
        dataLabels: {
          enabled: false
        },
        fill: {
          gradient: {
            enabled: true,
            opacityFrom: 0.55,
            opacityTo: 0
          }
        },
        markers: {
          size: 5,
          colors: ["#000524"],
          strokeColor: "#00BAEC",
          strokeWidth: 3
        },
        series: [
          {
            data: data
          }
        ],
        tooltip: {
          theme: "dark"
        },
        xaxis: {
          type: "datetime"
        },
        yaxis: {
          min: 0,
          tickAmount: 4
        }
      };

      var chart1 = new ApexCharts(
        document.querySelector("#chart-area"),
        options1
      );

      chart1.render();

      var options2 = {
        chart: {
          id: "chart1",
          height: 130,
          type: "bar",
          foreColor: "#ccc",
          brush: {
            target: "chart2",
            enabled: true
          },
          selection: {
            enabled: true,
            fill: {
              color: "#fff",
              opacity: 0.4
            },
            xaxis: {
              min: new Date("27 Jul 2017 10:00:00").getTime(),
              max: new Date("14 Aug 2017 10:00:00").getTime()
            }
          }
        },
        colors: ["#FF0080"],
        series: [
          {
            data: data
          }
        ],
        stroke: {
          width: 2
        },
        grid: {
          borderColor: "#444"
        },
        markers: {
          size: 0
        },
        xaxis: {
          type: "datetime",
          tooltip: {
            enabled: false
          }
        },
        yaxis: {
          tickAmount: 2
        }
      };

      var chart2 = new ApexCharts(
        document.querySelector("#chart-bar"),
        options2
      );

      chart2.render();
    }
  },
  mounted() {
    http
      .get("/youtuber/detail/trend/subscriberCount/" + 728 + "_" + 100)
      .then(response => {
        this.render(response.data.data);
      })
      .catch(err => {
        err;
      });
  }
};
</script>
<style scoped>
</style>
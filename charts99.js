let chart;

function updateChart(scores) {

    const ctx = document.getElementById("riskChart");

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: scores.map((_, i) => "Chat " + (i+1)),
            datasets: [{
                label: "Risk Score",
                data: scores
            }]
        }
    });
}

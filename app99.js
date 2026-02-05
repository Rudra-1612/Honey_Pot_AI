async function loadStats() {
    const res = await fetch("/stats");
    const data = await res.json();

    document.getElementById("scams").innerText = data.total_scams;
    document.getElementById("chats").innerText = data.active_chats;

    document.getElementById("logs").innerText =
        data.logs.join("\n");

    updateChart(data.risk_scores);
}

setInterval(loadStats, 2000);
loadStats();

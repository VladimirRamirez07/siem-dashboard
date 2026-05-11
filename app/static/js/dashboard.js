let eventChart, severityChart;

async function fetchStats() {
    const res = await fetch('/api/stats');
    const data = await res.json();

    document.getElementById('total').textContent = data.total;
    document.getElementById('high').textContent = data.severity.HIGH;
    document.getElementById('medium').textContent = data.severity.MEDIUM;
    document.getElementById('failed').textContent = data.failed_events;

    updateEventChart(data.event_types);
    updateSeverityChart(data.severity);
}

async function fetchLogs() {
    const res = await fetch('/api/logs');
    const logs = await res.json();
    const tbody = document.getElementById('logs-table');
    tbody.innerHTML = '';

    logs.forEach(log => {
        tbody.innerHTML += `
            <tr>
                <td>${log.timestamp}</td>
                <td>${log.event_type}</td>
                <td>${log.source_ip}</td>
                <td>${log.username}</td>
                <td class="sev-${log.severity}">${log.severity}</td>
                <td class="status-${log.status}">${log.status}</td>
                <td>${log.details}</td>
            </tr>`;
    });
}

async function fetchAlerts() {
    const res = await fetch('/api/alerts');
    const alerts = await res.json();
    const container = document.getElementById('alerts-container');
    container.innerHTML = '';

    if (alerts.length === 0) {
        container.innerHTML = '<p style="color:#7a9cc5">No active alerts</p>';
        return;
    }

    alerts.forEach(alert => {
        container.innerHTML += `
            <div class="alert-item alert-${alert.severity}">
                <span class="alert-badge badge-${alert.severity}">${alert.severity}</span>
                <span>${alert.event_type}</span>
                <span style="color:#7a9cc5">${alert.source_ip}</span>
                <span>${alert.details}</span>
                <span style="margin-left:auto;color:#7a9cc5;font-size:0.8rem">${alert.timestamp}</span>
            </div>`;
    });
}

function updateEventChart(eventTypes) {
    const labels = Object.keys(eventTypes);
    const values = Object.values(eventTypes);
    const colors = ['#f44336','#ff9800','#ffc107','#4caf50','#2196f3','#9c27b0'];

    if (eventChart) eventChart.destroy();

    eventChart = new Chart(document.getElementById('eventChart'), {
        type: 'doughnut',
        data: {
            labels,
            datasets: [{ data: values, backgroundColor: colors, borderWidth: 0 }]
        },
        options: {
            plugins: { legend: { labels: { color: '#e0e6ff' } } },
            responsive: true
        }
    });
}

function updateSeverityChart(severity) {
    if (severityChart) severityChart.destroy();

    severityChart = new Chart(document.getElementById('severityChart'), {
        type: 'bar',
        data: {
            labels: ['HIGH', 'MEDIUM', 'LOW'],
            datasets: [{
                label: 'Events',
                data: [severity.HIGH, severity.MEDIUM, severity.LOW],
                backgroundColor: ['#f44336', '#ffc107', '#4caf50'],
                borderRadius: 6
            }]
        },
        options: {
            plugins: { legend: { display: false } },
            scales: {
                y: { ticks: { color: '#7a9cc5' }, grid: { color: '#1e3a5f' } },
                x: { ticks: { color: '#7a9cc5' }, grid: { display: false } }
            },
            responsive: true
        }
    });
}

async function generateLogs() {
    const btn = document.querySelector('.btn-generate');
    btn.textContent = '⏳ Generating...';
    btn.disabled = true;

    await fetch('/api/generate');
    await Promise.all([fetchStats(), fetchLogs(), fetchAlerts()]);

    btn.textContent = '⚡ Generate Events';
    btn.disabled = false;
}

async function refreshAll() {
    await Promise.all([fetchStats(), fetchLogs(), fetchAlerts()]);
}

// Inicializar y auto-refresh cada 10 segundos
refreshAll();
setInterval(refreshAll, 10000);
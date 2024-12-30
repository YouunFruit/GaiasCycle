document.addEventListener("DOMContentLoaded", async () => {
    const tableBody = document.querySelector("tbody");

    try {
        const response = await fetch("/api/farms");
        if (!response.ok) throw new Error("Failed to fetch farms.");

        const farms = await response.json();
        tableBody.innerHTML = farms
            .map(farm => `
                <tr>
                    <td>${farm.id}</td>
                    <td>${farm.lat}, ${farm.lon}</td>
                    <td>${farm.size}</td>
                    <td>
                        <button class="btn btn-sm btn-primary" onclick="editFarm(${farm.id})">Edit</button>
                        <button class="btn btn-sm btn-danger" onclick="deleteFarm(${farm.id})">Delete</button>
                    </td>
                </tr>
            `).join('');
    } catch (error) {
        console.error("Error loading farms:", error);
    }
});

async function deleteFarm(farmId) {
    if (!confirm("Are you sure you want to delete this farm?")) return;

    try {
        const response = await fetch(`/api/farms/${farmId}`, { method: "DELETE" });
        if (!response.ok) throw new Error("Failed to delete farm.");
        alert("Farm deleted successfully.");
        location.reload();
    } catch (error) {
        console.error("Error deleting farm:", error);
    }
}

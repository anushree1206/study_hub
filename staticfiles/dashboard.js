function showDetails(type) {
    const detailsTitle = document.getElementById("details-title");
    const detailsContent = document.getElementById("details-content");
    const detailsSection = document.getElementById("details-section");

    let title, content;

    switch (type) {
        case "study":
            title = "📚 Study Materials";
            content = "Access high-quality study notes, PDFs, lecture videos, and subject-wise materials.";
            break;
        case "community":
            title = "👥 Community Support";
            content = "Join discussion forums, ask questions, and collaborate with peers and mentors.";
            break;
        case "technical":
            title = "🛠️ Technical Resources";
            content = "Explore coding platforms, engineering projects, and software tools for practical learning.";
            break;
        case "career":
            title = "🎯 Career Guidance";
            content = "Find roadmaps, internships, job preparation materials, and placement assistance.";
            break;
        case "labs":
            title = "🔬 Lab Manuals & Projects";
            content = "Access engineering lab manuals, experiments, and mini-project ideas.";
            break;
        case "events":
            title = "📅 Events & Hackathons";
            content = "Get information on upcoming hackathons, competitions, and workshops.";
            break;
        case "coding":
            title = "🎮 Coding Challenges";
            content = "Practice coding problems, take part in online coding contests, and improve your skills.";
            break;
        default:
            title = "Engineering Study Hub";
            content = "Select a category to view details.";
    }

    detailsTitle.innerText = title;
    detailsContent.innerText = content;
    detailsSection.classList.remove("hidden");
}

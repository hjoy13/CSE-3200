document.getElementById('reco-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const query = document.getElementById('query').value;

    // Send POST request to Flask backend
    const response = await fetch('/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ 'query': query })
    });

    try {
        const data = await response.json();

        // Display the recommendations
        let resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';  // Clear the results div before appending new results

        data.forEach(course => {
            const courseDiv = document.createElement('div');
            courseDiv.classList.add('card', 'p-3', 'mb-2');

            // Use safe checks to avoid displaying NaN or undefined values
            const title = course.title || 'No Title Available';
            const skills = course.skills_covered ? course.skills_covered.trim() : 'No skills covered available';
            
            // Ensure that 'NaN' values are handled properly
            const description = isNaN(course.description) ? 'No description available' : course.description;
            const duration = isNaN(course.duration) ? 'Duration not available' : course.duration;

            courseDiv.innerHTML = `
                <strong>${title}</strong>: ${skills}<br>
                <strong>Description:</strong> ${description}<br>
                <strong>Duration:</strong> ${duration}
            `;
            
            resultsDiv.appendChild(courseDiv);
        });
    } catch (error) {
        console.error('Error parsing response:', error);
    }
});

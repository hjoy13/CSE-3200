document.getElementById('reco-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const query = document.getElementById('query').value;

    // Show loading message
    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<div class="text-center">Loading recommendations...</div>';

    try {
        // Send POST request to Flask backend
        const response = await fetch('/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({ 'query': query })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Received data:', data); // Debug log

        // Clear the results div
        resultsDiv.innerHTML = '';

        if (!data || data.length === 0) {
            resultsDiv.innerHTML = '<div class="alert alert-info">No recommendations found for your query.</div>';
            return;
        }

        // Display the recommendations
        data.forEach(course => {
            const courseDiv = document.createElement('div');
            courseDiv.classList.add('card', 'p-3', 'mb-3', 'border');

            // Safe value extraction with proper null/undefined/NaN checking
            const title = course.title || 'No Title Available';
            const skills = course.skills_covered || 'No skills covered available';
            
            // Handle description - check for null, undefined, NaN (as string or number)
            let description = 'No description available';
            if (course.description && 
                course.description !== 'NaN' && 
                course.description !== null && 
                course.description !== undefined &&
                String(course.description).trim() !== '') {
                description = String(course.description).trim();
            }
            
            // Handle duration - check for null, undefined, NaN (as string or number)
            let duration = 'Duration not available';
            if (course.duration && 
                course.duration !== 'NaN' && 
                !isNaN(course.duration) && 
                course.duration !== null && 
                course.duration !== undefined) {
                duration = String(course.duration).trim();
            }

            // Handle level if available
            const level = course.level || 'Level not specified';
            const platform = course.platform || 'Platform not specified';
            const url = course.url || '#';

            courseDiv.innerHTML = `
                <div class="card-body">
                    <h5 class="card-title">${title}</h5>
                    <p class="card-text"><strong>Skills Covered:</strong> ${skills}</p>
                    <p class="card-text"><strong>Description:</strong> ${description}</p>
                    <p class="card-text">
                        <small class="text-muted">
                            <strong>Duration:</strong> ${duration} | 
                            <strong>Level:</strong> ${level} | 
                            <strong>Platform:</strong> ${platform} |
                            <strong>Platform:</strong> ${rating} |
                            <strong>Platform:</strong> ${students}

                        </small>
                    </p>
                    ${url !== '#' ? `<a href="${url}" target="_blank" class="btn btn-primary btn-sm">View Course</a>` : ''}
                </div>
            `;
            
            resultsDiv.appendChild(courseDiv);
        });

    } catch (error) {
        console.error('Error fetching recommendations:', error);
        resultsDiv.innerHTML = `
            <div class="alert alert-danger">
                <strong>Error:</strong> Failed to get recommendations. Please try again.
                <br><small>Details: ${error.message}</small>
            </div>
        `;
    }
});
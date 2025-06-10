function minOperation(locations) {
    const frequencyMap = new Map();
    
    // Count the frequency of each location
    for (const loc of locations) {
        frequencyMap.set(loc, (frequencyMap.get(loc) || 0) + 1);
    }
    
    let maxFrequency = 0;
    for (const count of frequencyMap.values()) {
        if (count > maxFrequency) {
            maxFrequency = count;
        }
    }
    
    const totalProducts = locations.length;
    return Math.max(maxFrequency, Math.ceil(totalProducts / 2));
}
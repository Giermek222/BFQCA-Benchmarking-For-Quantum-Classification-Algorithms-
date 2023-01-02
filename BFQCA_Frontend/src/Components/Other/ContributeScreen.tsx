const ContributeScreen = () => {
    return (
        <div>
            <h1>Hook allows to automatically compute benchmarking results for custom implementations of quantum algorithms.
To do so, set any of the **required** flags to "custom", and provide a file with the code of the algorithm/dataset/encoding.

Requirements:
1. File must contain a class named EXACTLY like the file name. Example: CustomAlgorithm.py has CustomAlgorithm class
2. File must be of .py extension
3. Only a selected amount of external libraries are available. See the list in requirements.py
4. A class inside the file must implement a selected interface from cowskit library. Either cowskit.algorithms.Algorithm, cowskit.datasets.Dataset or cowskit.encodings.Encoding
</h1>
        </div>
    )
}
export default ContributeScreen
import { useState, type ChangeEvent } from 'react';
import axios from 'axios';

function App() {
  const [sketchURL, setSketchURL] = useState<string>('');

  const handleImageUpload = async (e: ChangeEvent<HTMLInputElement>) => {
    const image = e.target.files?.[0];

    if (!image) return;

    const formData = new FormData();
    formData.append('file', image);

    try {
      const response = await axios.post(
        'http://localhost:8000/image/noodlefy',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
          responseType: 'blob',
        },
      );

      const blob = response.data;
      const url = URL.createObjectURL(blob);
      setSketchURL(url);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="w-screen h-screen flex items-center justify-center bg-stone-700">
      <div>
        <label htmlFor="img">Upload Image</label>
        <input name="img" type="file" onChange={handleImageUpload} />
      </div>

      {sketchURL && <img src={sketchURL} />}
    </div>
  );
}

export default App;

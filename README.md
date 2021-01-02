<img width="465" src="https://user-images.githubusercontent.com/57855070/103459200-114fe500-4d16-11eb-864b-ac377df14e3b.png">

### running:
python3 gale_and_shapley_algorithm.py

### Explanation of using the software:
After running, the following GUI window will open: <br />
<img width="200" src="https://user-images.githubusercontent.com/57855070/103459306-0ea1bf80-4d17-11eb-86a4-08ee4100949d.png">

You need to insert a file in the following format: <br />
>student: <br />
>Student Name: [First Preference,Second Preference,...,Preference N] <br />
>. <br />
>. <br />
>Student Name: [First Preference,Second Preference,...,Preference N] <br />
><br />
>university: <br />
>University Name: [First Preference,Second Preference,...,Preference N] <br />
>. <br />
>. <br />
>University Name: [First Preference,Second Preference,...,Preference N] <br />
> <br />

A concrete example:
>student: <br />
>ryan: [Yale,Harvard,NYU,MIT] <br />
>josh: [Harvard,Yale,MIT,NYU] <br />
>blake: [Harvard,MIT,NYU,Yale] <br />
>connor: [Yale,Harvard,NYU,MIT] <br />
> <br />
>university: <br />
>Yale: [ryan,blake,josh,connor] <br />
>Harvard: [ryan,blake,connor,josh] <br />
>NYU: [connor,josh,ryan,blake] <br />
>MIT: [ryan,josh,connor,blake] <br />
> <br />

**pay attention!** If the format is not working properly it will not work. <br />
**Note** the number of students and the number of universities must be the same.

After clicking the submit button you will get an answer in the same window, as follows: <br />
<img width="200" src="https://user-images.githubusercontent.com/57855070/103459700-cfc13900-4d19-11eb-9292-4b2e21466a2a.png">

After a few seconds the window closes automatically.

### Explanation of the algorithm:
[wikipedia](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm)
A good explanation on [YouTube]https://www.youtube.com/watch?v=FhRf0j068ZA), according to which I implemented the algorithm

### Credit:
[YouTube](https://www.youtube.com/watch?v=FhRf0j068ZA), [repository](https://github.com/Schachte/stable-matching-algorithm)







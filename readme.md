# Digital Image Processing(DIP) Practicals
>
# Image negative transformation
>
> `s=L-1-r`
>
> s -> value of pixel after processing,
>
> r -> value of pixe before processing,
>
> L -> maximum possible value of the intensity,
>
> `L=2^n`
>
> n -> number of bits required to represent the maximum possible value of intensity in the image.
>
# Image log transformation
>
> `s=c*log(1+r)`
>
> c -> positive constant,
>
> s -> value of pixel after processing,
>
> r -> value of pixe before processing
>
# Image power law transformation
>
> `s=c*r^g`
>
> s -> value of pixel after processing,
>
> r -> value of pixe before processing,
>
> c -> positive constant,
>
> g(gamma) -> positive constant
>
# Histogram
>
> - In Digital Image Processing, histogram is used for graphical representation of digital image.
>
> - A graph is plot by the number of pixels for each tonal value.
>
> ![A digital image](/digital%20image.PNG "Digital Image")
>
> #### Intensity-frequency table for the above image is
>
> ![Intensity-frequency table](/frequencyTable.PNG "intensity-frequency table")
>
> i -> intensity,
> n<sub>i</sub> -> frequency of intensity 'i'
>#### Histogram of the above table with reference to intensity-frequency table is
>
>![Histogram](/digitalImageHistogram.png "Histogram of the image")
>
# Image contrast stretching
>
> ![Formula](/contrast%20stretching.PNG "Contrast stretching formula")
>
> l -> output intensity,
>
> l<sub>max</sub> -> maximum intensity of the image,
>
> l<sub>min</sub> -> minimum intensity of the image,
>
> m<sub>min</sub> -> minimum pixel value,
>
> m<sub>max</sub> -> maximum pixel value,
>
> m -> Gray Level
>
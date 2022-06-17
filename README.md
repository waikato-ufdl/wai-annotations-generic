# wai-annotations-generic
wai.annotations module to make it easier to plugin custom code into a wai.annotations pipeline.

The manual is available here:

https://ufdl.cms.waikato.ac.nz/wai-annotations-manual/

## Plugins

TODO

## Examples

The following examples have the test classes linked for guidance on developing your own plugins.

### Audio classification

* [Source](src/wai/annotations/generic/source/audio_classification/test/_TestAC.py)
  ```bash
  wai-annotations convert \
    generic-source-ac \
      -c wai.annotations.generic.source.audio_classification.test.TestAC \
      -o "--dir /some/where/" \  # dir with .wav files
    generic-sink-ac \
      -c wai.annotations.generic.sink.audio_classification.test.TestAC \
      -o "--output label"
  ```

* [ISP](src/wai/annotations/generic/isp/audio_classification/test/_TestAC.py)
  ```bash
  wai-annotations convert \
    from-audio-files-ac \
      -i "/some/where/*.wav" \
    generic-isp-ac \
      -c wai.annotations.generic.isp.audio_classification.test.TestAC \
      -o "--output filename" \
    to-void-ac
  ```

* [Sink](src/wai/annotations/generic/sink/audio_classification/test/_TestAC.py)
  ```bash
  wai-annotations convert \
    from-audio-files-ac \
      -i "/some/where/*.wav" \
    generic-sink-ac \
      -c wai.annotations.generic.sink.audio_classification.test.TestAC \
      -o "--output filename"
  ```

### Image classification

* [Source](src/wai/annotations/generic/source/image_classification/test/_TestIC.py)
  ```bash
  wai-annotations convert \
    generic-source-ic \
      -c wai.annotations.generic.source.image_classification.test.TestIC \
      -o "--dir /some/where/" \  # dir with .jpg files
    generic-sink-ic \
      -c wai.annotations.generic.sink.image_classification.test.TestIC \
      -o "--output label"
  ```
  
* [ISP](src/wai/annotations/generic/isp/image_classification/test/_TestIC.py)
  ```bash
  wai-annotations convert \
    from-images-ic \
      -i "/some/where/*.jpg" \
    generic-isp-ic \
      -c wai.annotations.generic.isp.image_classification.test.TestIC \
      -o "--output dimensions" \
    to-void-ic
  ```

* [Sink](src/wai/annotations/generic/sink/image_classification/test/_TestIC.py)
  ```bash
  wai-annotations convert \
    from-images-ic \
      -i "/some/where/*.jpg" \
    generic-sink-ic \
      -c wai.annotations.generic.sink.image_classification.test.TestIC \
      -o "--output dimensions"
  ```

### Image segmentation

* [Source](src/wai/annotations/generic/source/image_segmentation/test/_TestIS.py)
  ```bash
  wai-annotations convert \
    generic-source-is \
      -c wai.annotations.generic.source.image_segmentation.test.TestIS \
      -o "--labels A B C --dir /some/where/" \    # dir with .jpg files
    generic-sink-is \
      -c wai.annotations.generic.sink.image_segmentation.test.TestIS \
      -o "--output dimensions"

  ```

* [ISP](src/wai/annotations/generic/isp/image_segmentation/test/_TestIS.py)
  ```bash
  wai-annotations convert \
    from-images-is \
      -i "/some/where/*.jpg" \
    generic-isp-is \
      -c wai.annotations.generic.isp.image_segmentation.test.TestIS \
      -o "--output dimensions" \
    to-void-is
  ```

* [Sink](src/wai/annotations/generic/sink/image_segmentation/test/_TestIS.py)
  ```bash
  wai-annotations convert \
    from-images-is \
      -i "/some/where/*.jpg" \
    generic-sink-is \
      -c wai.annotations.generic.sink.image_segmentation.test.TestIS \
      -o "--output dimensions"
  ```

### Object Detection

* [Source](src/wai/annotations/generic/source/object_detection/test/_TestOD.py)
  ```bash
  wai-annotations convert \
    generic-source-od \
      -c wai.annotations.generic.source.object_detection.test.TestOD \
      -o "--dir /some/where/" \   # dir with .jpg files
    generic-sink-od \
      -c wai.annotations.generic.sink.object_detection.test.TestOD \
      -o "--output num_objects"
  ```

* [ISP](src/wai/annotations/generic/isp/object_detection/test/_TestOD.py)
  ```bash
  wai-annotations convert \
    from-images-od \
      -i "/some/where/*.jpg" \
    generic-isp-od \
      -c wai.annotations.generic.isp.object_detection.test.TestOD \
      -o "--output dimensions" \
    to-void-od
  ```

* [Sink](src/wai/annotations/generic/sink/object_detection/test/_TestOD.py)
  ```bash
  wai-annotations convert \
    from-images-od \
      -i "/some/where/*.jpg" \
    generic-sink-od \
      -c wai.annotations.generic.sink.object_detection.test.TestOD \
      -o "--output dimensions"
  ```

### Speech

* [Source](src/wai/annotations/generic/source/speech/test/_TestSP.py)
  ```bash
  wai-annotations convert \
    generic-source-sp \
      -c wai.annotations.generic.source.speech.test.TestSP \
      -o "--dir /some/where/" \  # dir with .wav files
    generic-sink-ac \
      -c wai.annotations.generic.sink.speech.test.TestSP \
      -o "--output label"
  ```

* [ISP](src/wai/annotations/generic/isp/speech/test/_TestSP.py)
  ```bash
  wai-annotations convert \
    from-audio-files-sp \
      -i "/some/where/*.wav" \
    generic-isp-sp \
      -c wai.annotations.generic.isp.speech.test.TestSP \
      -o "--output filename" \
    to-void-sp
  ```

* [Sink](src/wai/annotations/generic/sink/speech/test/_TestSP.py)
  ```bash
  wai-annotations convert \
    from-audio-files-sp \
      -i "/some/where/*.wav" \
    generic-sink-sp \
      -c wai.annotations.generic.sink.speech.test.TestSP \
      -o "--output filename"
  ```

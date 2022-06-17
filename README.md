# wai-annotations-generic
wai.annotations module to make it easier to plugin custom code into a wai.annotations pipeline.

The manual is available here:

https://ufdl.cms.waikato.ac.nz/wai-annotations-manual/

## Plugins

TODO

## Examples

The following examples have the test classes linked for guidance on developing your own plugins.

### Image classification

* Source
  ```bash
  TODO
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

* Source
  ```bash
  TODO
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

* Source
  ```bash
  TODO
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

* Source
  ```bash
  TODO
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

### Audio classification

* Source
  ```bash
  TODO
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

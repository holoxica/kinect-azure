{
  'targets': [
    {
      "target_name": "kinectAzure",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "conditions": [
          [ "OS=='linux'", {
              "cflags+": [ "-std=c++11", "-fexceptions" ],
              "cflags_c+": [ "-std=c++11", "-fexceptions" ],
              "cflags_cc+": [ "-std=c++11", "-fexceptions" ],
          }],
          [ "OS=='freebsd'", {
              "cflags+": [ "-std=c++11", "-fexceptions" ],
              "cflags_c+": [ "-std=c++11", "-fexceptions" ],
              "cflags_cc+": [ "-std=c++11", "-fexceptions" ],
          }],
          [ "OS=='mac'", {
              "cflags+": [ "-stdlib=libc++" ],
              "xcode_settings": {
                  "OTHER_CPLUSPLUSFLAGS" : [ "-std=c++11", "-stdlib=libc++", "-pthread" ],
                  "OTHER_LDFLAGS": [ "-stdlib=libc++" ],
                  "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                  "MACOSX_DEPLOYMENT_TARGET": "10.7",
                  "CLANG_CXX_LANGUAGE_STANDARD":"c++11",
                  "CLANG_CXX_LIBRARY": "libc++"
              },
          }],
          [
          "OS=='win'", {
            "cflags": [
              "-Wall"
            ],
            "defines": [
              "WIN"
            ],
            "msvs_settings": {
              "VCCLCompilerTool": {
                "ExceptionHandling": "2",
                "DisableSpecificWarnings": [
                  "4244"
                ],
              }
            }
          }]
      ],
      "sources": [ "src/kinect_azure.cc" ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "<(module_root_dir)/sdk/sensor-sdk-1.4.0/build/native/include",
        "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/build/native/include"
      ],
      "libraries": [
        "<(module_root_dir)/sdk/sensor-sdk-1.4.0/lib/native/amd64/release/k4a.lib",
        "<(module_root_dir)/sdk/sensor-sdk-1.4.0/lib/native/amd64/release/k4arecord.lib",
        "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/lib/native/amd64/release/k4abt.lib"
      ],
      "copies": [
        {
          "destination": "<(module_root_dir)/build/Release",
          "files": [
            "<(module_root_dir)/sdk/sensor-sdk-1.4.0/lib/native/amd64/release/depthengine_2_0.dll",
            "<(module_root_dir)/sdk/sensor-sdk-1.4.0/lib/native/amd64/release/k4a.dll",
            "<(module_root_dir)/sdk/sensor-sdk-1.4.0/lib/native/amd64/release/k4arecord.dll",
            "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/lib/native/amd64/release/k4abt.dll",
            "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/lib/native/amd64/release/onnxruntime.dll",
            "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/content/dnn_model_2_0.onnx",
            "<(module_root_dir)/sdk/body-tracking-dependencies/lib/native/amd64/release/cublas64_100.dll",
            "<(module_root_dir)/sdk/body-tracking-dependencies/lib/native/amd64/release/cudart64_100.dll",
            "<(module_root_dir)/sdk/body-tracking-dependencies/lib/native/amd64/release/vcomp140.dll",
            "<(module_root_dir)/sdk/cudnn/lib/native/amd64/release/cudnn64_7.dll",
          ]
        }
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}

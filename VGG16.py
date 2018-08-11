{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "VGG16.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "metadata": {
        "id": "cr7oB5zW9Yio",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "!wget \"https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz\""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "57xcXSlmE0Ov",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "!apt-get -qq install -y libsm6 libxext6 && pip install -q -U opencv-python"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "6BaF16AUAguY",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "!tar -xf 'cifar-10-python.tar.gz'"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "bHWWwOHC-Tli",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "7fd3c73b-5330-46d7-fa18-3ec83dee8157"
      },
      "cell_type": "code",
      "source": [
        "# !cd cifar-10-batches-py\n",
        "# cd cifar-10-batches-py/\n",
        "# !pwd\n",
        "# cd data_batch_1\n",
        "# cd ../..\n",
        "ls"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\u001b[0m\u001b[01;34mcifar-10-batches-py\u001b[0m/  cifar-10-python.tar.gz  \u001b[01;34mdatalab\u001b[0m/\r\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "ac1CuMliDDg_",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "def processImages(images):\n",
        "  pro_data = []\n",
        "  for i in range(len(images)):\n",
        "    img_R = images[i][0:1024].reshape((32, 32))\n",
        "    img_G = images[i][1024:2048].reshape((32, 32))\n",
        "    img_B = images[i][2048:3072].reshape((32, 32))\n",
        "    img = np.dstack((img_R, img_G, img_B))\n",
        "    r_img = cv2.resize(img, (224,224))\n",
        "    pro_data.append(r_img)\n",
        "  return np.array(pro_data)\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "jKtK15Xq9mPK",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "import pickle\n",
        "import numpy as np\n",
        "import cv2\n",
        "file = '/content/cifar-10-batches-py/data_batch_1'\n",
        "with open(file, 'rb') as fo:\n",
        "  dict = pickle.load(fo, encoding='latin1')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "uyM4sLDhCL5M",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "8fd9243c-3214-47ee-a6c4-d911a6d38813"
      },
      "cell_type": "code",
      "source": [
        "from keras.utils import to_categorical\n",
        "from sklearn.utils import shuffle\n",
        "imageTrain, encodedTrain = shuffle(processImages(dict['data']),to_categorical(dict['labels']))"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Using TensorFlow backend.\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "metadata": {
        "id": "3_KTAlu9wpTW",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "abrB6LpbEn7e",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 367
        },
        "outputId": "1699c81b-2f32-4898-af79-6d6719c3817d"
      },
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import tensorflow as tf\n",
        "\n",
        "def normalize_production(self,x):\n",
        "        #this function is used to normalize instances in production according to saved training set statistics\n",
        "        # Input: X - a training set\n",
        "        # Output X - a normalized training set according to normalization constants.\n",
        "\n",
        "        #these values produced during first training and are general for the standard cifar10 training set normalization\n",
        "        mean = 120.707\n",
        "        std = 64.15\n",
        "        return (x-mean)/(std+1e-7)\n",
        "\n",
        "# sess = tf.InteractiveSession()\n",
        "\n",
        "rnd = np.random.randint(0,len(imageTrain))\n",
        "plt.imshow(imageTrain[rnd]/255.0)\n",
        "plt.show()\n",
        "# print(sess.run(tf.argmax(encodedTrain[rnd])))\n",
        "print(imageTrain[rnd].shape)\n",
        " "
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\necDlH+9l+NAzchUuKYw5+gZmWR1yPP9QTk30rKcd+5Y540Q1lRooQl5o1m+QOQtLPevAfmelh+gd\nl8W4gj1RDw8PjysfV7An6maZAHt1vEr0tpkcdvThvjTXZ0aKkro9abXgHrJt9Z+MnTXlfmkTQAX3\noVJA3Qf6vfzeTp/RFzI91IWenu62+Rpc0S/IJVvZc+9F5qF78rI/kgIeHh4e/0/hw3kPDw+PKuCN\nqIeHh0cV8EbUw8PDowp4I+rh4eFRBbwR9fDw8KgC3oh6eHh4VAFvRD08PDyqwIBttn/jjTewf/9+\nMMbw+uuv44477qgb7U2bNmHv3r0ol8tYsmQJdu3ahUOHDmHYsGEAgIULF+Lhhx+uGf2Ojg6sXLkS\nt9xyCwDg1ltvxaJFi9DS0oIoijBy5Ehs3rwZpVKpZjwAwHfffYf29nZTPnjwIMaPH48LFy6gqakJ\nALBmzRqMHz++JvQPHz6MpUuXYsGCBWhubsbff/+dK4P29nZ8+eWX4Jxjzpw5mD17dk15WLt2Lcrl\nMoIgwObNmzFy5EiMGzcOEydONNd98cUX5v2U/c1Da2trrj7WUg55fKxYsQKnTp0CAJw+fRp33XUX\nlixZgunTpxudGD58OLZs2dJvPLhjc8KECXXXiV5DDgA6Ojrk4sWLpZRSHjlyRM6ZM6dutHfv3i0X\nLVokpZTy5MmT8qGHHpJr1qyRu3btqhsPe/bskcuXL7eOtba2yh07dkgppXznnXfktm3b6saPlEmf\ntLW1yebmZvnnn3/WnN758+dlc3OzXLdunfz666+llPkyOH/+vJw2bZo8e/asvHjxonz66aflqVOn\nasZDS0uL/OGHH6SUUm7dulVu3LhRSinlvffe2y80e8JDnj7WUg5FfFC0trbK/fv3y2PHjsmZM2f2\nG12KvLFZb53oCwYknN+9ezcee+wxAMDNN9+MM2fO4N9//60L7XvuuQfvvvsuAOCqq67CxYsXEUVR\nN1fVHh0dHXj00UcBAI888gh2795dV/offPABli5dWjd6pVIJn3zyCUaNGmWO5clg//79mDBhAoYO\nHYrGxkZMnDgR+/btqxkPGzZswBNPPAEg8bJOnz7dL7R6w0MeaimH7vg4evQozp07V/NoMW9s1lsn\n+oIBMaJdXV0YPny4KY8YMQKdnZ11oS2EMKHq9u3b8eCDD0IIga1bt2L+/Pl49dVXcfLkyZrzceTI\nEbz88suYN28efv31V1y8eNGE71dffXXd5AEAv//+O6677jqMHDkSALBlyxa8+OKLWL9+Pf7777+a\n0AyCAI2NjdaxPBl0dXVhxIgRpk5/6koeD01NTRBCIIoifPPNN5g+fToA4NKlS1i9ejXmzp2Lzz//\nvF/oF/EAIKOPtZRDJT4A4KuvvkJzc7Mpd3V1YcWKFZg7d66VDqoWeWOz3jrRF1wRLyCRA/D4/k8/\n/YTt27fjs88+w8GDBzFs2DCMHTsWH3/8Md5//32sX7++ZrRvvPFGLFu2DE8++SSOHTuG+fPnW95w\nveWxfft2zJw5EwAwf/583HbbbRgzZgw2bNiAbdu2YeHChXXlByiWQT1kE0URWlpaMHnyZEyZMgUA\n0NLSghkzZoAxhubmZkyaNAkTJkyoCf1nnnkmo4933323VadeOnLp0iXs3bsXbW1tAIBhw4Zh5cqV\nmDFjBs6dO4fZs2dj8uTJ3XrSvQEdm9OmTTPHB1InKmFAPNFRo0ahq6vLlP/55x/jBdUDv/zyCz78\n8EN88sknGDp0KKZMmYKxY8cCAKZOnYrDhw/XlP7o0aPx1FNPgTGGMWPG4JprrsGZM2eM13f8+PF+\nVcru0NHRYQbp448/jjFjxgCojywompqaMjLI05Vay2bt2rW44YYbsGzZMnNs3rx5GDx4MJqamjB5\n8uSayiVPHwdCDgDw22+/WWH8kCFD8NxzzyEMQ4wYMQLjx4/H0aNH+42eOzavFJ2ohAExovfffz92\n7twJADh06BBGjRqFIUOG1IX2uXPnsGnTJnz00Udm9XP58uU4duwYgMSg6FXzWqG9vR2ffvopAKCz\nsxMnTpzArFmzjEx+/PFHPPDAAzXlQeP48eMYPHgwSqUSpJRYsGABzp49C6A+sqC47777MjK48847\nceDAAZw9exbnz5/Hvn37MGnSpJrx0N7ejjAMsWLFCnPs6NGjWL16NaSUKJfL2LdvX03lkqeP9ZaD\nxoEDB3D77beb8p49e/Dmm28CAC5cuIA//vgDN910U7/QyhubV4JOdIcBCecnTpyIcePGYe7cuWCM\nYcOGDXWjvWPHDpw6dQqrVq0yx2bNmoVVq1Zh0KBBaGpqMkpSK0ydOhWvvfYafv75Z1y+fBltbW0Y\nO3Ys1qxZg2+//RbXX389nn322ZryoNHZ2WnyS4wxzJkzBwsWLMCgQYMwevRoLF++vCZ0Dx48iI0b\nN+Kvv/5CEATYuXMn3n77bbS2tloyCMMQq1evxsKFC8EYwyuvvIKhQ4fWjIcTJ06goaEBL730EoBk\n4bOtrQ3XXnstnn/+eXDOMXXq1H5bZMnjobm5OaOPjY2NNZNDER/vvfceOjs7TWQCAJMmTcL333+P\nF154AVEUYfHixRg9enS/8JA3Nt966y2sW7eubjrRF/j3iXp4eHhUAf/EkoeHh0cV8EbUw8PDowp4\nI+rh4eFRBbwR9fDw8KgC3oh6eHh4VAFvRD08PDyqgDeiHh4eHlXg/wB8+YxQvuRh3QAAAABJRU5E\nrkJggg==\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7f1a53d70470>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "(224, 224, 3)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "HLBWIH2xys5K",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "n_classes = 10\n",
        "diemension = 3\n",
        "mu = 0\n",
        "sigma = 0.1\n",
        "\n",
        "\n",
        "x = tf.placeholder(tf.float32,shape=[None,224,224,3])\n",
        "y = tf.placeholder(tf.float32,shape=[None,n_classes])\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "mRBVzm7w2cnn",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "35c106a1-ea26-4804-a60b-fdeb20fd86a9"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 1\n",
        "weights_l1 = tf.Variable(tf.truncated_normal([3,3,3,64], mean=mu , stddev=sigma))\n",
        "biases_l1 = tf.Variable(tf.truncated_normal([64]))\n",
        "\n",
        "outlayer = tf.nn.conv2d(x, weights_l1, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l1\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu:0\", shape=(?, 224, 224, 64), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "fFwgysqH2hs4",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "87d4ecba-17b2-4624-84c1-5e31daf8c1eb"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 2\n",
        "weights_l2 = tf.Variable(tf.truncated_normal([3,3,64,64], mean=mu , stddev=sigma))\n",
        "biases_l2 = tf.Variable(tf.truncated_normal([64]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l2, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l2\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_1:0\", shape=(?, 224, 224, 64), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "djW-20Zj5RbQ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d991aad0-1d16-4ae4-a544-43c82a1212c8"
      },
      "cell_type": "code",
      "source": [
        "# MaxPooling 1\n",
        "outlayer = tf.nn.max_pool(outlayer, ksize=[1,2,2,1], strides=[1,2,2,1], padding=\"VALID\")\n",
        "print(outlayer)"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"MaxPool:0\", shape=(?, 112, 112, 64), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "wvsV8Yw4G130",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d0699a17-cc0c-49e1-f4ae-e39535b7d86c"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 3\n",
        "weights_l3 = tf.Variable(tf.truncated_normal([3,3,64,128], mean=mu , stddev=sigma))\n",
        "biases_l3 = tf.Variable(tf.truncated_normal([128]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l3, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l3\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_2:0\", shape=(?, 224, 224, 128), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "eu17vsCVF-s_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "e9220528-293c-4bda-a25d-a80f166cf52a"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 4\n",
        "weights_l4 = tf.Variable(tf.truncated_normal([3,3,128,128], mean=mu , stddev=sigma))\n",
        "biases_l4 = tf.Variable(tf.truncated_normal([128]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l4, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l4\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_3:0\", shape=(?, 224, 224, 128), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "LKgpTJ-xQp2z",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "7265f830-2923-4c6f-84c8-e1c0e331c6fe"
      },
      "cell_type": "code",
      "source": [
        "# MaxPooling 2\n",
        "outlayer = tf.nn.max_pool(outlayer, ksize=[1,2,2,1], strides=[1,2,2,1], padding=\"VALID\")\n",
        "print(outlayer)"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"MaxPool:0\", shape=(?, 112, 112, 128), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "cM_BKP9eU69m",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        "### **Convolutional Layer 3**"
      ]
    },
    {
      "metadata": {
        "id": "SdzbDXcgSQeB",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "e1d6c320-5f68-4706-8222-4c4d37c506e0"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 5\n",
        "weights_l5 = tf.Variable(tf.truncated_normal([3,3,128,256], mean=mu , stddev=sigma))\n",
        "biases_l5 = tf.Variable(tf.truncated_normal([256]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l5, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l5\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_4:0\", shape=(?, 112, 112, 256), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "M5JwfC-CTJ9_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d15b5a43-80ae-4028-cce0-b6d61265aea4"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 6\n",
        "weights_l6 = tf.Variable(tf.truncated_normal([3,3,256,256], mean=mu , stddev=sigma))\n",
        "biases_l6 = tf.Variable(tf.truncated_normal([256]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l6, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l6\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_5:0\", shape=(?, 112, 112, 256), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "lmOKIC5SSWqz",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "ea239fdd-cc16-464c-adcd-2e879fffaed3"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 7\n",
        "weights_l7 = tf.Variable(tf.truncated_normal([3,3,256,256], mean=mu , stddev=sigma))\n",
        "biases_l7 = tf.Variable(tf.truncated_normal([256]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l7, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l7\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_6:0\", shape=(?, 112, 112, 256), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "Rb0MYD0MVRCk",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d9c36182-f6bb-41a1-e49b-b77240553ed5"
      },
      "cell_type": "code",
      "source": [
        "# MaxPooling 1\n",
        "outlayer = tf.nn.max_pool(outlayer, ksize=[1,2,2,1], strides=[1,2,2,1], padding=\"VALID\")\n",
        "print(outlayer)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"MaxPool_1:0\", shape=(?, 56, 56, 256), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "LYnpe_GNVslH",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        "### **Convolutional 4**"
      ]
    },
    {
      "metadata": {
        "id": "lVIyhMFIVhy2",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "3f1877ff-86fb-4c53-b594-2cea04308d90"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 8\n",
        "weights_l8 = tf.Variable(tf.truncated_normal([3,3,256,512], mean=mu , stddev=sigma))\n",
        "biases_l8 = tf.Variable(tf.truncated_normal([512]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l8, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l8\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_7:0\", shape=(?, 56, 56, 512), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "k2VDBr49WCwF",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "5310b6b8-79cb-4f0b-c161-c0c0d604490a"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 9\n",
        "weights_l9 = tf.Variable(tf.truncated_normal([3,3,512,512], mean=mu , stddev=sigma))\n",
        "biases_l9 = tf.Variable(tf.truncated_normal([512]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l9, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l9\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_8:0\", shape=(?, 56, 56, 512), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "1hBtgxjUWTg2",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "5109272c-3a10-41f0-c7ef-bb22ae4887ab"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 10\n",
        "weights_l10 = tf.Variable(tf.truncated_normal([3,3,512,512], mean=mu , stddev=sigma))\n",
        "biases_l10 = tf.Variable(tf.truncated_normal([512]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l10, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l10\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_9:0\", shape=(?, 56, 56, 512), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "cBX7u0vaWbHP",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "e83e5fa1-9850-48e5-9510-748772100593"
      },
      "cell_type": "code",
      "source": [
        "# MaxPooling 4\n",
        "outlayer = tf.nn.max_pool(outlayer, ksize=[1,2,2,1], strides=[1,2,2,1], padding=\"VALID\")\n",
        "print(outlayer)"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"MaxPool_2:0\", shape=(?, 28, 28, 512), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "_N7cyGiQWwdf",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        "### **Colvolutional 5**"
      ]
    },
    {
      "metadata": {
        "id": "OvCOA0lhW2Vr",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "9c840b30-f3e4-4175-ab33-8b892381f678"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 11\n",
        "weights_l11 = tf.Variable(tf.truncated_normal([3,3,512,512], mean=mu , stddev=sigma))\n",
        "biases_l11 = tf.Variable(tf.truncated_normal([512]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l11, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l11\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_10:0\", shape=(?, 28, 28, 512), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "B-Nl1tH9XK43",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "8106738a-d948-4a6b-bb23-e23af10cd3cc"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 12\n",
        "weights_l12 = tf.Variable(tf.truncated_normal([3,3,512,512], mean=mu , stddev=sigma))\n",
        "biases_l12 = tf.Variable(tf.truncated_normal([512]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l12, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l12\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_11:0\", shape=(?, 28, 28, 512), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "vfVfq-mOXOTF",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "97034652-1259-4dfe-c38b-101dfc6d6819"
      },
      "cell_type": "code",
      "source": [
        "# Convolution 13\n",
        "weights_l13 = tf.Variable(tf.truncated_normal([3,3,512,512], mean=mu , stddev=sigma))\n",
        "biases_l13 = tf.Variable(tf.truncated_normal([512]))\n",
        "\n",
        "\n",
        "outlayer = tf.nn.conv2d(outlayer, weights_l13, [1,1,1,1], padding=\"SAME\")\n",
        "outlayer += biases_l13\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_12:0\", shape=(?, 28, 28, 512), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "IMkwJCTLXS9e",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d611b7c5-8f77-4fcc-d429-b3d5ffbeb388"
      },
      "cell_type": "code",
      "source": [
        "# MaxPooling 5\n",
        "outlayer = tf.nn.max_pool(outlayer, ksize=[1,2,2,1], strides=[1,2,2,1], padding=\"VALID\")\n",
        "print(outlayer)"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"MaxPool_3:0\", shape=(?, 14, 14, 512), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "dy0yoHxUYHhh",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        "### **Flatting Neuron**"
      ]
    },
    {
      "metadata": {
        "id": "STq2XC6sXVG2",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "450d562b-2589-495c-f0c3-bcf8527dd2b5"
      },
      "cell_type": "code",
      "source": [
        "# Flatting \n",
        "flattened = tf.reshape(outlayer, [-1, 7*7*512])\n",
        "print(flattened)"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Reshape:0\", shape=(?, 25088), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "W5ISPMaecIKD",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        "### **FC LAYERS**"
      ]
    },
    {
      "metadata": {
        "id": "ZbcYgW61cLa0",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "618cbd3e-0f7b-48a2-b8d8-30647909d0fd"
      },
      "cell_type": "code",
      "source": [
        "#FC 1 \n",
        "wd1 = tf.Variable(tf.truncated_normal([7*7*512 , 4096], mean=mu , stddev=sigma))\n",
        "bd1 = tf.Variable(tf.truncated_normal([4096]))\n",
        "\n",
        "outlayer = tf.matmul(flattened, wd1) + bd1\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_13:0\", shape=(?, 4096), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "2WoBcOSTcax9",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "99981273-ab26-45d4-dd1d-0ad26a47ae48"
      },
      "cell_type": "code",
      "source": [
        "#FC 2\n",
        "wd2 = tf.Variable(tf.truncated_normal([4096 , 4096], mean=mu , stddev=sigma))\n",
        "bd2 = tf.Variable(tf.truncated_normal([4096]))\n",
        "\n",
        "outlayer = tf.matmul(outlayer, wd2) + bd2\n",
        "outlayer = tf.nn.relu(outlayer)\n",
        "print(outlayer)"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"Relu_14:0\", shape=(?, 4096), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "yOxvq9gdgVDH",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "#Output Layer\n",
        "wd0 = tf.Variable(tf.truncated_normal([4096, 10], mean=mu , stddev=sigma))\n",
        "bd0 = tf.Variable(tf.truncated_normal([10]))\n",
        "outlayer = tf.matmul(outlayer, wd0) + bd0\n",
        "outlayer = tf.nn.relu(outlayer)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "Lp-Wx9uEclDV",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 173
        },
        "outputId": "b80dad0b-0bd5-4bfc-a7fc-012792379c5d"
      },
      "cell_type": "code",
      "source": [
        "pred = tf.nn.softmax(outlayer)\n",
        "\n",
        "loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=outlayer))\n",
        "optimizer = tf.train.AdamOptimizer(0.0001) # learning rate\n",
        "train = optimizer.minimize(loss)\n",
        "correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(pred, 1))\n",
        "total_prediction = tf.reduce_sum(tf.cast(correct_prediction, tf.float32))\n",
        "accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "WARNING:tensorflow:From <ipython-input-28-6b5d0e803050>:3: softmax_cross_entropy_with_logits (from tensorflow.python.ops.nn_ops) is deprecated and will be removed in a future version.\n",
            "Instructions for updating:\n",
            "\n",
            "Future major versions of TensorFlow will allow gradients to flow\n",
            "into the labels input on backprop by default.\n",
            "\n",
            "See @{tf.nn.softmax_cross_entropy_with_logits_v2}.\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "NATu-0tNdFYV",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "sess = tf.InteractiveSession()\n",
        "tf.global_variables_initializer().run()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "cjQFbRZYedJK",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        "### **Traing**"
      ]
    },
    {
      "metadata": {
        "id": "Y-dFUetSeacD",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "def trainModel_v2():\n",
        "  batch_size = 128\n",
        "  for epoch in range(20):\n",
        "    epoch_loss = 0 \n",
        "    total_accuracy = 0\n",
        "    for offset in range(0, len(imageTrain), batch_size):\n",
        "      end = offset + batch_size\n",
        "      batch_x = imageTrain[offset:end]\n",
        "      batch_y = encodedTrain[offset:end]\n",
        "      accuracy_in_batch = sess.run(total_prediction, feed_dict={x: batch_x, y: batch_y})\n",
        "      print(accuracy_in_batch)\n",
        "#       total_accuracy += accuracy_in_batch\n",
        "#     print(\"Epoch \",epoch, \" Epoch Loss \",epoch_loss, \" Accuracy Total \", total_accuracy/len(imageTrain) * 100)\n",
        "\n",
        "\n",
        "def trainModel_v1():\n",
        "  batch_size = 50\n",
        "  for epoch in range(20):\n",
        "    epoch_loss = 0 \n",
        "    total_accuracy = 0\n",
        "    for offset in range(0, len(imageTrain), batch_size):\n",
        "      end = offset + batch_size\n",
        "      batch_x = imageTrain[offset:end]\n",
        "      batch_y = encodedTrain[offset:end]\n",
        "      c = sess.run(loss, feed_dict={x: batch_x, y: batch_y})\n",
        "      accuracy_in_batch = sess.run(total_prediction, feed_dict={x: batch_x, y: batch_y})\n",
        "      total_accuracy += accuracy_in_batch\n",
        "      epoch_loss += c\n",
        "      print(c)\n",
        "      print(accuracy_in_batch)\n",
        "    print(\"Epoch \",epoch, \" Epoch Loss \",epoch_loss, \" Accuracy Total \", total_accuracy/len(imageTrain) * 100)\n",
        "#       print(sess.run(pred, feed_dict={x: batch_x}))\n",
        "#       print(sess.run(correct_prediction, feed_dict={x: batch_x, y: batch_y}))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "zeHXoHxPfSea",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 2394
        },
        "outputId": "576deaca-78ca-4bbe-c500-86164327ae39"
      },
      "cell_type": "code",
      "source": [
        "trainModel_v2()\n",
        "# trainModel_v1()"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ResourceExhaustedError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mResourceExhaustedError\u001b[0m                    Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tensorflow/python/client/session.py\u001b[0m in \u001b[0;36m_do_call\u001b[0;34m(self, fn, *args)\u001b[0m\n\u001b[1;32m   1277\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1278\u001b[0;31m       \u001b[0;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1279\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0merrors\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mOpError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tensorflow/python/client/session.py\u001b[0m in \u001b[0;36m_run_fn\u001b[0;34m(feed_dict, fetch_list, target_list, options, run_metadata)\u001b[0m\n\u001b[1;32m   1262\u001b[0m       return self._call_tf_sessionrun(\n\u001b[0;32m-> 1263\u001b[0;31m           options, feed_dict, fetch_list, target_list, run_metadata)\n\u001b[0m\u001b[1;32m   1264\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tensorflow/python/client/session.py\u001b[0m in \u001b[0;36m_call_tf_sessionrun\u001b[0;34m(self, options, feed_dict, fetch_list, target_list, run_metadata)\u001b[0m\n\u001b[1;32m   1349\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_session\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfeed_dict\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfetch_list\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtarget_list\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1350\u001b[0;31m         run_metadata)\n\u001b[0m\u001b[1;32m   1351\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mResourceExhaustedError\u001b[0m: OOM when allocating tensor with shape[128,224,224,128] and type float on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc\n\t [[Node: Conv2D_2 = Conv2D[T=DT_FLOAT, data_format=\"NHWC\", dilations=[1, 1, 1, 1], padding=\"SAME\", strides=[1, 1, 1, 1], use_cudnn_on_gpu=true, _device=\"/job:localhost/replica:0/task:0/device:GPU:0\"](Relu_1, Variable_4/read)]]\nHint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.\n\n\t [[Node: Sum/_11 = _Recv[client_terminated=false, recv_device=\"/job:localhost/replica:0/task:0/device:CPU:0\", send_device=\"/job:localhost/replica:0/task:0/device:GPU:0\", send_device_incarnation=1, tensor_name=\"edge_170_Sum\", tensor_type=DT_FLOAT, _device=\"/job:localhost/replica:0/task:0/device:CPU:0\"]()]]\nHint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.\n",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mResourceExhaustedError\u001b[0m                    Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-34-2df2415297ae>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtrainModel_v2\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;31m# trainModel_v1()\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-32-45c45e1c8347>\u001b[0m in \u001b[0;36mtrainModel_v2\u001b[0;34m()\u001b[0m\n\u001b[1;32m      8\u001b[0m       \u001b[0mbatch_x\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mimageTrain\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0moffset\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m       \u001b[0mbatch_y\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mencodedTrain\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0moffset\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m       \u001b[0maccuracy_in_batch\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtotal_prediction\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfeed_dict\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mbatch_x\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mbatch_y\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m       \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maccuracy_in_batch\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;31m#       total_accuracy += accuracy_in_batch\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tensorflow/python/client/session.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self, fetches, feed_dict, options, run_metadata)\u001b[0m\n\u001b[1;32m    875\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    876\u001b[0m       result = self._run(None, fetches, feed_dict, options_ptr,\n\u001b[0;32m--> 877\u001b[0;31m                          run_metadata_ptr)\n\u001b[0m\u001b[1;32m    878\u001b[0m       \u001b[0;32mif\u001b[0m \u001b[0mrun_metadata\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    879\u001b[0m         \u001b[0mproto_data\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtf_session\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTF_GetBuffer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrun_metadata_ptr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tensorflow/python/client/session.py\u001b[0m in \u001b[0;36m_run\u001b[0;34m(self, handle, fetches, feed_dict, options, run_metadata)\u001b[0m\n\u001b[1;32m   1098\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mfinal_fetches\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinal_targets\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mhandle\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mfeed_dict_tensor\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1099\u001b[0m       results = self._do_run(handle, final_targets, final_fetches,\n\u001b[0;32m-> 1100\u001b[0;31m                              feed_dict_tensor, options, run_metadata)\n\u001b[0m\u001b[1;32m   1101\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1102\u001b[0m       \u001b[0mresults\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tensorflow/python/client/session.py\u001b[0m in \u001b[0;36m_do_run\u001b[0;34m(self, handle, target_list, fetch_list, feed_dict, options, run_metadata)\u001b[0m\n\u001b[1;32m   1270\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mhandle\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1271\u001b[0m       return self._do_call(_run_fn, feeds, fetches, targets, options,\n\u001b[0;32m-> 1272\u001b[0;31m                            run_metadata)\n\u001b[0m\u001b[1;32m   1273\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1274\u001b[0m       \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_do_call\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_prun_fn\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhandle\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfeeds\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfetches\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tensorflow/python/client/session.py\u001b[0m in \u001b[0;36m_do_call\u001b[0;34m(self, fn, *args)\u001b[0m\n\u001b[1;32m   1289\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1290\u001b[0m           \u001b[0;32mpass\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1291\u001b[0;31m       \u001b[0;32mraise\u001b[0m \u001b[0mtype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnode_def\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mop\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmessage\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1292\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1293\u001b[0m   \u001b[0;32mdef\u001b[0m \u001b[0m_extend_graph\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mResourceExhaustedError\u001b[0m: OOM when allocating tensor with shape[128,224,224,128] and type float on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc\n\t [[Node: Conv2D_2 = Conv2D[T=DT_FLOAT, data_format=\"NHWC\", dilations=[1, 1, 1, 1], padding=\"SAME\", strides=[1, 1, 1, 1], use_cudnn_on_gpu=true, _device=\"/job:localhost/replica:0/task:0/device:GPU:0\"](Relu_1, Variable_4/read)]]\nHint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.\n\n\t [[Node: Sum/_11 = _Recv[client_terminated=false, recv_device=\"/job:localhost/replica:0/task:0/device:CPU:0\", send_device=\"/job:localhost/replica:0/task:0/device:GPU:0\", send_device_incarnation=1, tensor_name=\"edge_170_Sum\", tensor_type=DT_FLOAT, _device=\"/job:localhost/replica:0/task:0/device:CPU:0\"]()]]\nHint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.\n\n\nCaused by op 'Conv2D_2', defined at:\n  File \"/usr/lib/python3.6/runpy.py\", line 193, in _run_module_as_main\n    \"__main__\", mod_spec)\n  File \"/usr/lib/python3.6/runpy.py\", line 85, in _run_code\n    exec(code, run_globals)\n  File \"/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py\", line 16, in <module>\n    app.launch_new_instance()\n  File \"/usr/local/lib/python3.6/dist-packages/traitlets/config/application.py\", line 658, in launch_instance\n    app.start()\n  File \"/usr/local/lib/python3.6/dist-packages/ipykernel/kernelapp.py\", line 477, in start\n    ioloop.IOLoop.instance().start()\n  File \"/usr/local/lib/python3.6/dist-packages/zmq/eventloop/ioloop.py\", line 177, in start\n    super(ZMQIOLoop, self).start()\n  File \"/usr/local/lib/python3.6/dist-packages/tornado/ioloop.py\", line 888, in start\n    handler_func(fd_obj, events)\n  File \"/usr/local/lib/python3.6/dist-packages/tornado/stack_context.py\", line 277, in null_wrapper\n    return fn(*args, **kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/zmq/eventloop/zmqstream.py\", line 440, in _handle_events\n    self._handle_recv()\n  File \"/usr/local/lib/python3.6/dist-packages/zmq/eventloop/zmqstream.py\", line 472, in _handle_recv\n    self._run_callback(callback, msg)\n  File \"/usr/local/lib/python3.6/dist-packages/zmq/eventloop/zmqstream.py\", line 414, in _run_callback\n    callback(*args, **kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/tornado/stack_context.py\", line 277, in null_wrapper\n    return fn(*args, **kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/ipykernel/kernelbase.py\", line 283, in dispatcher\n    return self.dispatch_shell(stream, msg)\n  File \"/usr/local/lib/python3.6/dist-packages/ipykernel/kernelbase.py\", line 235, in dispatch_shell\n    handler(stream, idents, msg)\n  File \"/usr/local/lib/python3.6/dist-packages/ipykernel/kernelbase.py\", line 399, in execute_request\n    user_expressions, allow_stdin)\n  File \"/usr/local/lib/python3.6/dist-packages/ipykernel/ipkernel.py\", line 196, in do_execute\n    res = shell.run_cell(code, store_history=store_history, silent=silent)\n  File \"/usr/local/lib/python3.6/dist-packages/ipykernel/zmqshell.py\", line 533, in run_cell\n    return super(ZMQInteractiveShell, self).run_cell(*args, **kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/IPython/core/interactiveshell.py\", line 2718, in run_cell\n    interactivity=interactivity, compiler=compiler, result=result)\n  File \"/usr/local/lib/python3.6/dist-packages/IPython/core/interactiveshell.py\", line 2822, in run_ast_nodes\n    if self.run_code(code, result):\n  File \"/usr/local/lib/python3.6/dist-packages/IPython/core/interactiveshell.py\", line 2882, in run_code\n    exec(code_obj, self.user_global_ns, self.user_ns)\n  File \"<ipython-input-9-3122460988eb>\", line 5, in <module>\n    outlayer = tf.nn.conv2d(outlayer, weights_l3, [1,1,1,1], padding=\"SAME\")\n  File \"/usr/local/lib/python3.6/dist-packages/tensorflow/python/ops/gen_nn_ops.py\", line 956, in conv2d\n    data_format=data_format, dilations=dilations, name=name)\n  File \"/usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/op_def_library.py\", line 787, in _apply_op_helper\n    op_def=op_def)\n  File \"/usr/local/lib/python3.6/dist-packages/tensorflow/python/util/deprecation.py\", line 454, in new_func\n    return func(*args, **kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/ops.py\", line 3155, in create_op\n    op_def=op_def)\n  File \"/usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/ops.py\", line 1717, in __init__\n    self._traceback = tf_stack.extract_stack()\n\nResourceExhaustedError (see above for traceback): OOM when allocating tensor with shape[128,224,224,128] and type float on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc\n\t [[Node: Conv2D_2 = Conv2D[T=DT_FLOAT, data_format=\"NHWC\", dilations=[1, 1, 1, 1], padding=\"SAME\", strides=[1, 1, 1, 1], use_cudnn_on_gpu=true, _device=\"/job:localhost/replica:0/task:0/device:GPU:0\"](Relu_1, Variable_4/read)]]\nHint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.\n\n\t [[Node: Sum/_11 = _Recv[client_terminated=false, recv_device=\"/job:localhost/replica:0/task:0/device:CPU:0\", send_device=\"/job:localhost/replica:0/task:0/device:GPU:0\", send_device_incarnation=1, tensor_name=\"edge_170_Sum\", tensor_type=DT_FLOAT, _device=\"/job:localhost/replica:0/task:0/device:CPU:0\"]()]]\nHint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.\n\n"
          ]
        }
      ]
    }
  ]
}
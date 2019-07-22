
import tensorflow as tf

def printTensors(pb_file):

    # read pb into graph_def
    with tf.gfile.GFile(pb_file, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        names = [n.name for n in graph_def.node]
        print (names[0])
        print (names[-1])


printTensors("graph_unoptimized.pb")

from tensorflow import flags

FLAGS = flags.FLAGS

if __name__ == "__main__":
  flags.DEFINE_string('model','net','model name')
  print(FLAGS.model)

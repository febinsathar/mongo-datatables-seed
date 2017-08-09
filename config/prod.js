module.exports = {
  mongodb: {
    host: 'localhost',
    port: 27017,
    dbname: 'test',
    username: '',
    password: '',
    get connectionUri() {
      return 'mongodb://' + this.host + ':' + this.port + '/' + this.dbname;
    }
  }
}
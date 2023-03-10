from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from data.jobs import Jobs
from data import db_session
from data.parser_jobs import parser


def abort_if_job_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"Job {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_job_not_found(jobs_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(jobs_id)
        return jsonify({'jobs': job.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished'))})

    def delete(self, jobs_id):
        abort_if_job_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, jobs_id):
        abort_if_job_not_found(jobs_id)
        args = parser.parse_args()
        session = db_session.create_session()
        job = session.query(Jobs).filter(Jobs.id == jobs_id).first()
        job.team_leader = args['team_leader']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.is_finished = args['is_finished']
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})
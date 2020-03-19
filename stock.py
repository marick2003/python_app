import datetime
import concurrent.futures
from flask import Flask, render_template, jsonify
from twstock.stock import Stock
from twstock.analytics import BestFourPoint